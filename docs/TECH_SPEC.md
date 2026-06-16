# TECH_SPEC.md – Meshopt

---

## 1. Overview

**Meshopt** is a service‑mesh management and optimization platform that simplifies configuration, monitoring, and troubleshooting for developers and organizations.  
It exposes a unified API for provisioning, configuring, and observing service‑mesh resources (e.g., Envoy, Istio, Linkerd) while providing automated performance tuning, policy enforcement, and diagnostics.

The platform is built as a set of micro‑services that communicate over gRPC and REST, orchestrated by Kubernetes. It leverages open‑source tooling (Istio, Envoy, Prometheus, Grafana, Jaeger) and internal libraries (vLLM for inference‑based recommendations, SGLang for structured generation of configs).

---

## 2. Architecture

```
+-------------------+          +-------------------+          +-------------------+
|  Client API (REST)|<-------->|  API Gateway (gRPC)|<-------->|  Auth & Rate‑Limiting|
+-------------------+          +-------------------+          +-------------------+
          |                               |                               |
          v                               v                               v
+-------------------+          +-------------------+          +-------------------+
|  Config Service   |<------->|  Policy Service   |<------->|  Metrics Service  |
+-------------------+          +-------------------+          +-------------------+
          |                               |                               |
          v                               v                               v
+-------------------+          +-------------------+          +-------------------+
|  Envoy/ Istio API |          |  Optimization Engine|          |  Observability API|
+-------------------+          +-------------------+          +-------------------+
          |                               |                               |
          v                               v                               v
+-------------------+          +-------------------+          +-------------------+
|  Envoy/ Istio     |          |  vLLM + SGLang    |          |  Prometheus/Jaeger|
+-------------------+          +-------------------+          +-------------------+
```

### 2.1 Core Services

| Service | Responsibility | Primary Language | Key Dependencies |
|---------|----------------|------------------|------------------|
| **API Gateway** | Entry point, auth, rate‑limit, request routing | Go | gRPC, Envoy, JWT |
| **Config Service** | CRUD for mesh configs, validation, templating | Go | PostgreSQL, SGLang |
| **Policy Service** | Policy definition, enforcement, audit | Go | PostgreSQL, Envoy |
| **Metrics Service** | Collects, aggregates, exposes metrics | Go | Prometheus client, Jaeger |
| **Optimization Engine** | Generates performance recommendations | Python | vLLM, SGLang, Pandas |
| **Observability API** | Aggregates logs, traces, metrics | Go | Loki, Prometheus, Jaeger |

### 2.2 Data Flow

1. **Client** sends a REST request → **API Gateway** (auth, rate‑limit).  
2. Gateway forwards to **Config/Policy** services via gRPC.  
3. Config Service writes to **PostgreSQL** and triggers **Optimization Engine**.  
4. Optimization Engine uses **vLLM** to generate config suggestions, stores them in **SGLang** templates.  
5. Config changes are applied to the underlying mesh via **Envoy/Istio API**.  
6. **Metrics Service** pulls data from Prometheus/Jaeger, exposes via `/metrics`.  
7. Observability API aggregates logs from Loki, traces from Jaeger, and forwards to dashboards.

---

## 3. Data Model

### 3.1 Database Schema (PostgreSQL)

| Table | Columns | Notes |
|-------|---------|-------|
| `meshes` | `id PK`, `name`, `type`, `config_json`, `created_at`, `updated_at` | `type` ∈ {istio, envoy, linkerd} |
| `policies` | `id PK`, `mesh_id FK`, `policy_name`, `policy_json`, `created_at`, `updated_at` | |
| `recommendations` | `id PK`, `mesh_id FK`, `recommendation_json`, `generated_at`, `status` | `status` ∈ {pending, applied, rejected} |
| `audit_logs` | `id PK`, `user_id`, `action`, `resource_id`, `resource_type`, `timestamp`, `details` | |

### 3.2 API Payloads

```json
// Create Mesh
{
  "name": "prod-frontend",
  "type": "istio",
  "config": { ... }
}

// Policy Definition
{
  "mesh_id": "uuid",
  "policy_name": "latency-threshold",
  "policy": {
    "match": { "service": "frontend" },
    "action": "reject",
    "threshold_ms": 200
  }
}
```

---

## 4. Key APIs & Interfaces

### 4.1 REST Endpoints (API Gateway)

| Method | Path | Description |
|--------|------|-------------|
| POST | `/meshes` | Create a new mesh |
| GET | `/meshes/{id}` | Retrieve mesh config |
| PUT | `/meshes/{id}` | Update mesh config |
| DELETE | `/meshes/{id}` | Delete mesh |
| POST | `/meshes/{id}/policies` | Add policy |
| GET | `/meshes/{id}/policies` | List policies |
| POST | `/meshes/{id}/optimize` | Trigger optimization |
| GET | `/meshes/{id}/recommendations` | List recommendations |
| POST | `/meshes/{id}/recommendations/{rec_id}/apply` | Apply recommendation |
| GET | `/metrics` | Prometheus metrics endpoint |

### 4.2 gRPC Services

- **ConfigService** – CRUD, validation, templating
- **PolicyService** – Policy lifecycle, enforcement hooks
- **MetricsService** – Pull metrics, push alerts
- **OptimizationService** – Request optimization, fetch results

### 4.3 Envoy/Istio API

- **Envoy Admin API** – `/config_dump`, `/clusters`, `/listeners`
- **Istio Pilot API** – `/config/v1beta1/virtualservices`, `/config/v1beta1/destinationrules`

---

## 5. Technology Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **API Gateway** | Go, gRPC, Envoy | High performance, native gRPC support |
| **Config & Policy Services** | Go, PostgreSQL, SGLang | Strong typing, template generation |
| **Optimization Engine** | Python, vLLM, SGLang, Pandas | ML inference for recommendations |
| **Observability** | Go, Prometheus, Jaeger, Loki | Standard open‑source stack |
| **Container Runtime** | Docker, Kubernetes | Orchestration, scaling |
| **CI/CD** | GitHub Actions, Helm | Automated deployments |
| **Testing** | Go test, pytest, Postman | Unit & integration coverage |
| **Security** | JWT, OPA, RBAC | Fine‑grained access control |

---

## 6. Dependencies

| Component | Version | Source |
|-----------|---------|--------|
| Go | 1.22+ | Official |
| PostgreSQL | 15.x | Official |
| vLLM | 0.3.0 | `vllm-project/vllm` |
| SGLang | 0.4.1 | `sgl-project/sglang` |
| Envoy | 1.28.x | Official |
| Istio | 1.18.x | Official |
| Prometheus | 2.52.x | Official |
| Jaeger | 1.57.x | Official |
| Loki | 3.1.x | Official |
| Helm | 3.12.x | Official |
| Docker | 27.x | Official |
| Kubernetes | 1.30.x | Official |

---

## 7. Deployment

### 7.1 Helm Chart

- **Chart Name**: `meshopt`
- **Values**:
  - `image.repository`, `image.tag`
  - `postgresql.enabled`, `postgresql.postgresqlPassword`
  - `envoy.enabled`, `istio.enabled`
  - `optimizationEngine.resources`
  - `metrics.prometheus.enabled`
  - `auth.jwtSecret`

### 7.2 CI/CD Pipeline

1. **Lint**: `golangci-lint`, `flake8`
2. **Unit Tests**: `go test ./...`, `pytest -m unit`
3. **Integration Tests**: Spin up test cluster, run `go test -tags=integration`
4. **Build**: Docker images, push to registry
5. **Helm Lint**: `helm lint`
6. **Deploy**: `helm upgrade --install meshopt ./chart`

### 7.3 Observability

- **Prometheus** scrapes `/metrics` from each service.
- **Grafana** dashboards: `Mesh Health`, `Policy Violations`, `Optimization Impact`.
- **Jaeger** traces for request flow.
- **Loki** aggregates logs from all pods.

---

## 8. Security & Compliance

- **Authentication**: JWT bearer tokens; token introspection via Auth Service.
- **Authorization**: Role‑Based Access Control (RBAC) enforced by OPA policies.
- **Secrets Management**: Kubernetes Secrets + HashiCorp Vault integration.
- **Audit Logging**: All state‑changing actions logged to `audit_logs` table.
- **Data Encryption**: TLS for all external traffic; AES‑256 for stored secrets.

---

## 9. Performance & Scaling

- **Horizontal Pod Autoscaling** based on CPU/Memory and custom metrics (`meshopt_requests_per_second`).
- **Cache Layer**: Redis for hot config lookups (optional).
- **Batch Optimization**: Queue jobs via Kafka; process in parallel.
- **Observability**: Rate‑limit Prometheus scrapes to 1k/s.

---

## 10. Future Enhancements

1. **Multi‑Cluster Management** – support federated meshes.
2. **AI‑Driven Auto‑Scaling** – use vLLM to predict traffic patterns.
3. **Marketplace for Mesh Plugins** – allow third‑party extensions.
4. **GraphQL API** – for flexible client queries.

---

*Prepared by: Senior Product/Engineering Lead*  
*Date: 2026‑06‑16*

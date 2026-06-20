<h3 align="center">🛠️ Meshopt</h3>

<div align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.9-blue.svg" alt="Python 3.9" />
  </a>
  <a href="https://poetry.dev/">
    <img src="https://img.shields.io/badge/PyPoetry-1.1.12-blue.svg" alt="PyPoetry 1.1.12" />
  </a>
  <a href="https://github.com/pytest-dev/pytest">
    <img src="https://img.shields.io/badge/Pytest-6.2.5-blue.svg" alt="Pytest 6.2.5" />
  </a>
  <a href="https://github.com/axentx/meshopt/stargazers">
    <img src="https://img.shields.io/github/stars/axentx/meshopt.svg?style=social" alt="GitHub stars" />
  </a>
</div>

---

# 🚀 Meshopt

**Power microservices with a lightweight, Python-based service mesh.**

Meshopt is a minimal service-mesh implementation written in Python. It runs a central process that handles service discovery, request routing, and exposes a monitoring dashboard on a configurable HTTP port.

---

## Why Meshopt?

* **🔍 Simple and lightweight**: Meshopt is designed for local-only service mesh testing or prototyping.
* **🚀 Fast development**: Quickly spin up a service mesh for your microservices.
* **📊 Built-in monitoring**: Get insights into your service mesh with a built-in monitoring dashboard.
* **🤝 Easy configuration**: Configure Meshopt via a JSON file (config.json).
* **🚫 No external dependencies**: Meshopt doesn't rely on external databases or complex orchestration tools.
* **📚 Well-documented**: Find detailed documentation in the `docs` directory.

---

## Feature Overview

| Feature | Description |
| --- | --- |
| Service Discovery | Meshopt automatically discovers services and their endpoints. |
| Request Routing | Meshopt routes requests to the correct service endpoint. |
| Monitoring Dashboard | A built-in monitoring dashboard provides insights into your service mesh. |
| Configuration | Configure Meshopt via a JSON file (config.json). |

---

## Tech Stack

* Python
* Poetry
* Pytest

---

## Project Structure

* `business/`
* `docs/`
* `src/`
* `tests/`

---

## Getting Started

1. **Install dependencies**: Run `poetry install` to install the required dependencies.
2. **Run Meshopt**: Run `poetry run python src/meshopt.py` to start the Meshopt service.
3. **Test Meshopt**: Run `poetry run pytest tests/` to run the test suite.

---

## Deploy

To deploy Meshopt, follow these steps:

1. **Build the Docker image**: Run `poetry run docker build -t meshopt .` to build the Docker image.
2. **Run the Docker container**: Run `docker run -p 8080:8080 meshopt` to start the Meshopt service.

---

## Status

Meshopt is currently in the early stages of development. Recent commits:

* `9d8ec40 feat(meshopt): real, sandbox-tested implementation`
* `54fa5dc readme-keeper: generate proper project README (overview/stack/run/deploy)`
* `f0137d2 docs: add startup artifacts (PRD.md, REQUIREMENTS.md, TECH_SPEC.md, BMC.md, STORIES.md, ROADMAP.md) [artifact-prep]`
* `6325961 Initial commit`

---

## Contributing

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on contributing to Meshopt.

---

## License

Meshopt is licensed under the MIT License.
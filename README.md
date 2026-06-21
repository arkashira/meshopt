<h3 align="center">🛠️ Meshopt</h3>

<div align="center">
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://python.org)
  [![Build Status](https://img.shields.io/badge/Build-Passing-green.svg)](https://github.com/axentx/meshopt)
  [![Stars](https://img.shields.io/badge/Stars-⭐⭐⭐⭐⭐-yellow.svg)](https://github.com/axentx/meshopt)
</div>

---

# 🚀 Meshopt
**Power developers with lightweight service discovery and routing for local microservices.** Meshopt is a Python-based service mesh designed for local development and prototyping, providing essential service mesh functionality without complex dependencies.

## Why Meshopt?
- **Lightweight**: Minimal footprint with no external dependencies beyond Python standard libraries
- **Developer-friendly**: Simple JSON configuration for quick setup in local environments
- **Complete solution**: Handles service discovery, request routing, and monitoring in one package
- **Dashboard-driven**: Built-in HTTP dashboard for visualizing service interactions
- **Built for local development**: Perfect for testing microservices before deploying to production meshes
- **Zero-configuration**: Works out of the box with sensible defaults
- **Extensible**: Core functionality designed for easy customization

## Feature Overview
| Feature | Description |
|--------|-------------|
| Service Discovery | Automatically registers and tracks services in the mesh |
| Request Routing | Directs service-to-service requests based on configuration |
| Monitoring Dashboard | Real-time visualization of service interactions and health |
| JSON Configuration | Simple, human-readable configuration format |
| Local Development Focus | Optimized for development and prototyping environments |

## Tech Stack
- Python
- Poetry
- pytest

## Project Structure
```
meshopt/
├── business/          # Core business logic implementation
├── docs/             # Documentation files
├── src/              # Source code
└── tests/            # Test files
```

## Getting Started
```bash
# Clone the repository
git clone https://github.com/axentx/meshopt.git
cd meshopt

# Install dependencies with Poetry
poetry install

# Run the service mesh
poetry run python -m meshopt

# Run tests
poetry run pytest
```

## Deploy
```bash
# Build the project
poetry build

# Install the package
pip install dist/meshopt-*.whl
```

## Status
Early development stage with core functionality implemented. Recent commits focus on sandbox-tested implementation and proper documentation.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to Meshopt.

## License
This project is licensed under the MIT License.
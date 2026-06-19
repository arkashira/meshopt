import argparse
import json
from dataclasses import dataclass

@dataclass
class ServiceMeshConfig:
    services: list
    monitoring_port: int

def create_service_mesh_config(services, monitoring_port):
    return ServiceMeshConfig(services, monitoring_port)

def save_service_mesh_config(config, filename):
    with open(filename, 'w') as f:
        json.dump({
            'services': config.services,
            'monitoring_port': config.monitoring_port
        }, f)

def load_service_mesh_config(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return ServiceMeshConfig(data['services'], data['monitoring_port'])
    except json.JSONDecodeError as e:
        raise e

def main():
    parser = argparse.ArgumentParser(description='Meshopt Service Mesh')
    parser.add_argument('--config', help='Configuration file')
    parser.add_argument('--monitoring-port', type=int, help='Monitoring port')
    args = parser.parse_args()
    if args.config:
        config = load_service_mesh_config(args.config)
    else:
        services = ['service1', 'service2']
        config = create_service_mesh_config(services, args.monitoring_port or 8080)
    print(f'Service Mesh Config: {config}')

if __name__ == '__main__':
    main()

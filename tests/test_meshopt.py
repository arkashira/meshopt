import pytest
import json
from src.meshopt import create_service_mesh_config, load_service_mesh_config, save_service_mesh_config

def test_create_service_mesh_config():
    services = ['service1', 'service2']
    monitoring_port = 8080
    config = create_service_mesh_config(services, monitoring_port)
    assert config.services == services
    assert config.monitoring_port == monitoring_port

def test_save_and_load_service_mesh_config(tmp_path):
    services = ['service1', 'service2']
    monitoring_port = 8080
    config = create_service_mesh_config(services, monitoring_port)
    filename = tmp_path / 'config.json'
    save_service_mesh_config(config, str(filename))
    loaded_config = load_service_mesh_config(str(filename))
    assert loaded_config.services == services
    assert loaded_config.monitoring_port == monitoring_port

def test_load_service_mesh_config_invalid_file(tmp_path):
    filename = tmp_path / 'config.json'
    with open(str(filename), 'w') as f:
        f.write('Invalid JSON')
    with pytest.raises(json.JSONDecodeError):
        load_service_mesh_config(str(filename))

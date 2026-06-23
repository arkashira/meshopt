import pytest
import json
from meshopt import ServiceMesh, Dashboard

@pytest.fixture
def sample_dashboard():
    dash = Dashboard()
    dash.add_mesh(ServiceMesh(name="mesh1", mesh_type="istio", status="active", metrics={"latency": 120}))
    dash.add_mesh(ServiceMesh(name="mesh2", mesh_type="linkerd", status="inactive", metrics={"latency": 200}))
    dash.add_mesh(ServiceMesh(name="mesh3", mesh_type="istio", status="active", metrics={"latency": 80}))
    return dash

def test_list_meshes(sample_dashboard):
    meshes = sample_dashboard.list_meshes()
    assert len(meshes) == 3
    names = {m.name for m in meshes}
    assert names == {"mesh1", "mesh2", "mesh3"}

def test_filter_by_type(sample_dashboard):
    istio_meshes = sample_dashboard.filter_meshes(mesh_type="istio")
    assert len(istio_meshes) == 2
    for m in istio_meshes:
        assert m.mesh_type == "istio"

def test_filter_by_status_and_name(sample_dashboard):
    result = sample_dashboard.filter_meshes(name="mesh2", status="inactive")
    assert len(result) == 1
    assert result[0].name == "mesh2"
    assert result[0].status == "inactive"

def test_filter_no_match(sample_dashboard):
    result = sample_dashboard.filter_meshes(name="nonexistent")
    assert result == []

def test_sort_by_latency(sample_dashboard):
    sorted_meshes = sample_dashboard.sort_meshes(key=lambda m: m.metrics["latency"])
    names_in_order = [m.name for m in sorted_meshes]
    assert names_in_order == ["mesh3", "mesh1", "mesh2"]

def test_get_metrics(sample_dashboard):
    metrics = sample_dashboard.get_metrics("mesh1")
    assert metrics == {"latency": 120}
    with pytest.raises(ValueError):
        sample_dashboard.get_metrics("unknown")

def test_to_json(sample_dashboard):
    json_str = sample_dashboard.to_json()
    data = json.loads(json_str)
    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0]["name"] == "mesh1"
    assert data[0]["metrics"]["latency"] == 120

from meshopt import Meshopt, ServiceMesh

def test_add_service_mesh():
    meshopt = Meshopt()
    service_mesh = ServiceMesh("test", "type", "status", {"metric": 1})
    meshopt.add_service_mesh(service_mesh)
    assert len(meshopt.get_service_meshes()) == 1

def test_filter_service_meshes():
    meshopt = Meshopt()
    service_mesh1 = ServiceMesh("test1", "type1", "status1", {"metric": 1})
    service_mesh2 = ServiceMesh("test2", "type2", "status2", {"metric": 2})
    meshopt.add_service_mesh(service_mesh1)
    meshopt.add_service_mesh(service_mesh2)
    filtered_meshes = meshopt.filter_service_meshes(name="test1")
    assert len(filtered_meshes) == 1
    assert filtered_meshes[0].name == "test1"

def test_sort_service_meshes():
    meshopt = Meshopt()
    service_mesh1 = ServiceMesh("test1", "type1", "status1", {"metric": 1})
    service_mesh2 = ServiceMesh("test2", "type2", "status2", {"metric": 2})
    meshopt.add_service_mesh(service_mesh1)
    meshopt.add_service_mesh(service_mesh2)
    sorted_meshes = meshopt.sort_service_meshes("name")
    assert sorted_meshes[0].name == "test1"
    assert sorted_meshes[1].name == "test2"

def test_get_metrics():
    meshopt = Meshopt()
    service_mesh = ServiceMesh("test", "type", "status", {"metric": 1})
    meshopt.add_service_mesh(service_mesh)
    metrics = meshopt.get_metrics("test")
    assert metrics == {"metric": 1}

def test_get_metrics_not_found():
    meshopt = Meshopt()
    metrics = meshopt.get_metrics("test")
    assert metrics is None

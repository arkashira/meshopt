from meshopt import AutoScaler, MeshTraffic

def test_scale_up():
    scaler = AutoScaler(threshold=0.8, scale_up_timeout=2, scale_down_timeout=2)
    mesh_traffic = MeshTraffic(cpu_utilization=0.9)
    assert scaler.scale(mesh_traffic) == 2

def test_scale_down():
    scaler = AutoScaler(threshold=0.8, scale_up_timeout=2, scale_down_timeout=2)
    mesh_traffic = MeshTraffic(cpu_utilization=0.7)
    scaler.current_scale = 2
    scaler.last_scale_time = 2
    assert scaler.scale(mesh_traffic) == 1

def test_no_scale():
    scaler = AutoScaler(threshold=0.8, scale_up_timeout=2, scale_down_timeout=2)
    mesh_traffic = MeshTraffic(cpu_utilization=0.7)
    assert scaler.scale(mesh_traffic) == 1

def test_scale_up_timeout():
    scaler = AutoScaler(threshold=0.8, scale_up_timeout=2, scale_down_timeout=2)
    mesh_traffic = MeshTraffic(cpu_utilization=0.9)
    scaler.last_scale_time = 1
    assert scaler.scale(mesh_traffic) == 2

def test_scale_down_timeout():
    scaler = AutoScaler(threshold=0.8, scale_up_timeout=2, scale_down_timeout=2)
    mesh_traffic = MeshTraffic(cpu_utilization=0.7)
    scaler.current_scale = 2
    scaler.last_scale_time = 1
    assert scaler.scale(mesh_traffic) == 2

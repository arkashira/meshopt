import pytest
from meshopt import MeshOpt, Route

def test_suggest_optimizations():
    routes = [Route(1, 120), Route(2, 40), Route(3, 60)]
    meshopt = MeshOpt(routes)
    optimizations = meshopt.suggest_optimizations()
    assert len(optimizations) == 2
    assert optimizations[0]["route_id"] == 1
    assert optimizations[0]["optimization"] == "traffic_mirroring"
    assert optimizations[1]["route_id"] == 3
    assert optimizations[1]["optimization"] == "canary_routes"

def test_apply_optimization():
    routes = [Route(1, 120)]
    meshopt = MeshOpt(routes)
    optimization = {"route_id": 1, "optimization": "traffic_mirroring"}
    new_latency = meshopt.apply_optimization(optimization)
    assert new_latency == 110

def test_get_latency():
    routes = [Route(1, 120), Route(2, 40)]
    meshopt = MeshOpt(routes)
    latency = meshopt.get_latency(1)
    assert latency == 120
    latency = meshopt.get_latency(2)
    assert latency == 40
    latency = meshopt.get_latency(3)
    assert latency is None

import json
from dataclasses import dataclass
from typing import List

@dataclass
class Route:
    id: int
    latency: float

class MeshOpt:
    def __init__(self, routes: List[Route]):
        self.routes = routes

    def suggest_optimizations(self):
        optimizations = []
        for route in self.routes:
            if route.latency > 100:
                optimizations.append({"route_id": route.id, "optimization": "traffic_mirroring"})
            elif route.latency > 50:
                optimizations.append({"route_id": route.id, "optimization": "canary_routes"})
        return optimizations

    def apply_optimization(self, optimization):
        for route in self.routes:
            if route.id == optimization["route_id"]:
                if optimization["optimization"] == "traffic_mirroring":
                    route.latency -= 10
                elif optimization["optimization"] == "canary_routes":
                    route.latency -= 5
                return route.latency
        return None

    def get_latency(self, route_id):
        for route in self.routes:
            if route.id == route_id:
                return route.latency
        return None

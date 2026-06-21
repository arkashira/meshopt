import json
from dataclasses import dataclass
from typing import List

@dataclass
class ServiceMesh:
    name: str
    type: str
    status: str
    metrics: dict

class Meshopt:
    def __init__(self):
        self.service_meshes = []

    def add_service_mesh(self, service_mesh: ServiceMesh):
        self.service_meshes.append(service_mesh)

    def get_service_meshes(self):
        return self.service_meshes

    def filter_service_meshes(self, name=None, type=None, status=None):
        filtered_meshes = self.service_meshes
        if name:
            filtered_meshes = [mesh for mesh in filtered_meshes if mesh.name == name]
        if type:
            filtered_meshes = [mesh for mesh in filtered_meshes if mesh.type == type]
        if status:
            filtered_meshes = [mesh for mesh in filtered_meshes if mesh.status == status]
        return filtered_meshes

    def sort_service_meshes(self, key):
        return sorted(self.service_meshes, key=lambda x: getattr(x, key))

    def get_metrics(self, name):
        for mesh in self.service_meshes:
            if mesh.name == name:
                return mesh.metrics
        return None

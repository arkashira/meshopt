import json
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable, Optional

@dataclass
class ServiceMesh:
    """Represents a service mesh instance."""
    name: str
    mesh_type: str
    status: str
    metrics: Dict[str, Any] = field(default_factory=dict)

    def update_metrics(self, new_metrics: Dict[str, Any]) -> None:
        """Update the metrics dictionary with new values."""
        self.metrics.update(new_metrics)

    def to_dict(self) -> Dict[str, Any]:
        """Return a serializable representation."""
        return {
            "name": self.name,
            "type": self.mesh_type,
            "status": self.status,
            "metrics": self.metrics,
        }

class Dashboard:
    """Unified dashboard for managing multiple service meshes."""
    def __init__(self) -> None:
        self._meshes: List[ServiceMesh] = []

    def add_mesh(self, mesh: ServiceMesh) -> None:
        """Add a new service mesh to the dashboard."""
        self._meshes.append(mesh)

    def list_meshes(self) -> List[ServiceMesh]:
        """Return the list of all service meshes."""
        return list(self._meshes)

    def filter_meshes(
        self, *, name: Optional[str] = None, mesh_type: Optional[str] = None, status: Optional[str] = None,
    ) -> List[ServiceMesh]:
        """Filter meshes by name, type, and status."""
        result = self._meshes
        if name is not None:
            result = [m for m in result if m.name == name]
        if mesh_type is not None:
            result = [m for m in result if m.mesh_type == mesh_type]
        if status is not None:
            result = [m for m in result if m.status == status]
        return result

    def sort_meshes(
        self, key: Callable[[ServiceMesh], Any], reverse: bool = False,
    ) -> List[ServiceMesh]:
        """Return meshes sorted by a key function."""
        return sorted(self._meshes, key=key, reverse=reverse)

    def get_metrics(self, name: str) -> Dict[str, Any]:
        """Return metrics for a mesh with the given name."""
        for mesh in self._meshes:
            if mesh.name == name:
                return mesh.metrics
        raise ValueError(f"Mesh with name '{name}' not found")

    def to_json(self) -> str:
        """Serialize the dashboard state to JSON."""
        return json.dumps([m.to_dict() for m in self._meshes], indent=2)

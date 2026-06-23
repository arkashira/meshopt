import json
from dataclasses import dataclass
from typing import List

@dataclass
class MeshTraffic:
    cpu_utilization: float

class AutoScaler:
    def __init__(self, threshold: float, scale_up_timeout: int, scale_down_timeout: int):
        self.threshold = threshold
        self.scale_up_timeout = scale_up_timeout
        self.scale_down_timeout = scale_down_timeout
        self.current_scale = 1
        self.last_scale_time = 0

    def scale(self, mesh_traffic: MeshTraffic) -> int:
        if mesh_traffic.cpu_utilization > self.threshold:
            if self.current_scale < 10:
                self.current_scale += 1
                self.last_scale_time = 0
            return self.current_scale
        else:
            if self.current_scale > 1 and self.last_scale_time >= self.scale_down_timeout:
                self.current_scale -= 1
                self.last_scale_time = 0
            return self.current_scale

    def update(self):
        self.last_scale_time += 1

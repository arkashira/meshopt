import json
from dataclasses import dataclass
from datetime import datetime, timedelta
import argparse

@dataclass
class Optimization:
    confidence: float
    spec: str

class MeshOpt:
    def __init__(self):
        self.optimizations = []
        self.log = []

    def define_off_peak_window(self, start_time, end_time):
        self.off_peak_window = (start_time, end_time)

    def add_optimization(self, optimization):
        self.optimizations.append(optimization)

    def auto_apply_optimizations(self):
        for optimization in self.optimizations:
            if optimization.confidence >= 90:
                self.log.append(optimization.spec)
                print(f"Applied optimization: {optimization.spec}")

    def rollback(self):
        if self.log:
            last_spec = self.log.pop()
            print(f"Rolled back to: {last_spec}")
            return last_spec
        return None

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-time", help="Start time of off-peak window (HH:MM)")
    parser.add_argument("--end-time", help="End time of off-peak window (HH:MM)")
    parser.add_argument("--confidence", help="Confidence threshold for auto-apply (float)")
    parser.add_argument("--spec", help="Optimization spec to add")
    args = parser.parse_args()

    meshopt = MeshOpt()
    meshopt.define_off_peak_window(parse_time(args.start_time), parse_time(args.end_time))

    optimization = Optimization(float(args.confidence), args.spec)
    meshopt.add_optimization(optimization)

    meshopt.auto_apply_optimizations()

    rollback_spec = meshopt.rollback()
    if rollback_spec:
        print(f"Rolled back to: {rollback_spec}")

if __name__ == "__main__":
    main()

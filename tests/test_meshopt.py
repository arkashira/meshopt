from meshopt import MeshOpt, Optimization, parse_time
import pytest

def test_define_off_peak_window():
    meshopt = MeshOpt()
    start_time = parse_time("02:00")
    end_time = parse_time("04:00")
    meshopt.define_off_peak_window(start_time, end_time)
    assert meshopt.off_peak_window == (start_time, end_time)

def test_add_optimization():
    meshopt = MeshOpt()
    optimization = Optimization(90.0, "spec1")
    meshopt.add_optimization(optimization)
    assert len(meshopt.optimizations) == 1
    assert meshopt.optimizations[0] == optimization

def test_auto_apply_optimizations():
    meshopt = MeshOpt()
    optimization1 = Optimization(90.0, "spec1")
    optimization2 = Optimization(80.0, "spec2")
    meshopt.add_optimization(optimization1)
    meshopt.add_optimization(optimization2)
    meshopt.auto_apply_optimizations()
    assert len(meshopt.log) == 1
    assert meshopt.log[0] == "spec1"

def test_rollback():
    meshopt = MeshOpt()
    optimization = Optimization(90.0, "spec1")
    meshopt.add_optimization(optimization)
    meshopt.auto_apply_optimizations()
    rolled_back_spec = meshopt.rollback()
    assert rolled_back_spec == "spec1"
    assert len(meshopt.log) == 0

def test_rollback_empty_log():
    meshopt = MeshOpt()
    rolled_back_spec = meshopt.rollback()
    assert rolled_back_spec is None
    assert len(meshopt.log) == 0

def test_parse_time():
    time_str = "02:00"
    parsed_time = parse_time(time_str)
    assert parsed_time.hour == 2
    assert parsed_time.minute == 0

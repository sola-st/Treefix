# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/graph_building_test.py
num_ops = 100
num_iters = 10
duration = self._computeReadVariableOpDuration(num_ops, num_iters)
name = "BenchmarkReadVariableOp"
if flags.config().graph_building_optimization.value():
    name += "WithGraphBuildingOptimization"
self.report_benchmark(
    name=name,
    iters=num_iters,
    wall_time=duration,
    extras={"num_ops": num_ops})

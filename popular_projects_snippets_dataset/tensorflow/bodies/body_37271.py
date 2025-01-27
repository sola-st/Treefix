# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
iters = 10
# Run loop body on GPU, but other ops on CPU.
duration = self._runOneBenchmark("cpu", iters, static_unroll=False)
self.report_benchmark(
    name="while_op_cross_device", iters=iters, wall_time=duration)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
iters = 10
# Run loop body on GPU, but other ops on CPU.
duration = self._runOneBenchmark("cpu", iters, static_unroll=True)
self.report_benchmark(
    name="unroll_cross_device_cpu", iters=iters, wall_time=duration)

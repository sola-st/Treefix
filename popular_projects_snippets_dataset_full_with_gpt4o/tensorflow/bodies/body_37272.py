# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
iters = 10
# Run all ops on the same GPU device.
duration = self._runOneBenchmark("gpu", iters, static_unroll=False)
self.report_benchmark(
    name="while_op_same_device", iters=iters, wall_time=duration)

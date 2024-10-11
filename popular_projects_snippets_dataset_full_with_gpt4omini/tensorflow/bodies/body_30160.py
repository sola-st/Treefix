# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
self.evaluate(variables.global_variables_initializer())
for _ in range(10):
    _ = self.evaluate(slice_op)
iters = 1000
t0 = time.time()
for _ in range(iters):
    self.evaluate(slice_op)
t1 = time.time()
self.report_benchmark(iters=iters, wall_time=(t1 - t0) / 1000.0)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
self.evaluate(variables.global_variables_initializer())
for _ in range(warmup_iters):
    _ = self.evaluate(op)
t0 = time.time()
for _ in range(iters):
    self.evaluate(op)
t1 = time.time()
self.report_benchmark(iters=iters, wall_time=(t1 - t0) / float(iters))

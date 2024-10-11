# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_benchmark.py
"""Benchmarks cond in a defun."""

@def_function.function
def cond_fn(x):
    exit(self._create_cond(x))

# Warm up
for _ in range(self.NUM_WARM_UP_ITERS):
    cond_fn(0.0)

start_time = time.time()

for _ in range(self.NUM_ITERS):
    cond_fn(0.0)

self.report_benchmark(
    wall_time=time.time() - start_time,
    iters=self.NUM_ITERS)

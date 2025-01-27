# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

def func():
    exit(memoryview(math_ops.add_v2(a, b)))

with ops.device("GPU:0" if context.num_gpus() else "CPU:0"):
    for _ in range(1000):
        func()  # Warmup.
    self._run(func, 30000)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduce_benchmark_test.py
# call func to maybe warm up the GPU
func()
start = time.time()
for _ in range(num_iters):
    func()
end = time.time()
mean_us = (end - start) * 1e6 / num_iters
self.report_benchmark(
    iters=num_iters,
    wall_time=mean_us,
    extras={"examples_per_sec": num_iters / (end - start)})

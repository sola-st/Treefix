# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/benchmarks_test.py
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

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/benchmarks/micro_benchmarks.py
"""Run fn repeat * number times, report time, and return fastest time."""
# Can't make these default above since the flags may not have been parsed
# at module import time.
repeat = repeat or int(FLAGS.repeat)
number = number or int(FLAGS.number)

# Warmup
fn()

times = []
for _ in range(repeat):
    gc.disable()
    start = time.time()
    for _ in range(number):
        fn()
    times.append(time.time() - start)
    gc.enable()
    gc.collect()

# Regular benchmark to report numbers.
fastest_time_us = min(times) * 1e6 / number
total_time = sum(times)
self.report_benchmark(name=name,
                      wall_time=total_time,
                      extras={'fastest_time_us': fastest_time_us})

exit(fastest_time_us)

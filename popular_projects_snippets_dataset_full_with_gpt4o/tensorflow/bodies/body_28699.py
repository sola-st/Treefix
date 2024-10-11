# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py
"""Assert memory usage doesn't increase beyond given threshold for f."""

# Warm up.
f()
# Wait for background threads to start up and allocate memory.
time.sleep(4)
initial = memory_profiler.memory_usage(-1)[0]
for _ in range(num_iters):
    f()
increase = memory_profiler.memory_usage(-1)[0] - initial
logging.info("Memory increase observed: %f MB" % increase)
assert increase < max_increase_mb, (
    "Increase is too high. Initial memory usage: %f MB. Increase: %f MB. "
    "Maximum allowed increase: %f") % (initial, increase, max_increase_mb)

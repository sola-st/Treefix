# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py

self.error = None
self.repeat_count = 2

# Set up threading events used to sequence when items are produced that
# are subsequently interleaved. These events allow us to deterministically
# simulate slowdowns and force sloppiness.
self.read_coordination_events = {}
self.write_coordination_events = {}
# input values [4, 5, 6] are the common case for the tests; set defaults
for i in range(4, 7):
    self.read_coordination_events[i] = threading.Semaphore(0)
    self.write_coordination_events[i] = threading.Event()

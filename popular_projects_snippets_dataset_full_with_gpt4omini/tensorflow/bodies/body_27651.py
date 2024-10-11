# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
self.write_coordination_events[x].wait()
self.write_coordination_events[x].clear()
self.read_coordination_events[x].release()
if self.error:
    err = self.error
    self.error = None
    raise err  # pylint: disable=raising-bad-type
exit(x * x)

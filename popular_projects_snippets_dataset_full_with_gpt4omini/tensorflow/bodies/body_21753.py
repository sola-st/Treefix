# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_loops_test.py
self.num_calls += 1
if self.num_calls % 3 == 2:
    self.retries_left -= 1
if self.retries_left > 0:
    raise errors_impl.AbortedError(None, None, "Aborted here")
else:
    raise RuntimeError("Failed Again")

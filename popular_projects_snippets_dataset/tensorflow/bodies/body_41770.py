# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
# We don't count tracing when users load a concrete function directly or
# call get_concrete_function, so the first call can be not a tracing call.
if not self._calls_per_tracings:
    self._calls_per_tracings = [0]
self._calls_per_tracings[-1] += 1
self._call_count += 1

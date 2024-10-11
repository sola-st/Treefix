# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker.py
"""Take a memory snapshot for later analysis.

    `record_snapshot()` must be called once every iteration at the same
    location. This is because the detection algorithm relies on the assumption
    that if there is a leak, it's happening similarly on every snapshot.

    The recommended number of `record_snapshot()` call depends on the testing
    code complexity and the allcoation pattern.
    """
self._python_memory_checker.record_snapshot()
if CppMemoryChecker:
    self._cpp_memory_checker.record_snapshot()

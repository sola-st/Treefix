# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker.py
"""Raises an exception if a leak is detected.

    This algorithm classifies a series of allocations as a leak if it's the same
    type(Python) or it happens at the same stack trace(C++) at every snapshot,
    but possibly except one snapshot.
    """

self._python_memory_checker.assert_no_leak_if_all_possibly_except_one()
if CppMemoryChecker:
    self._cpp_memory_checker.assert_no_leak_if_all_possibly_except_one()

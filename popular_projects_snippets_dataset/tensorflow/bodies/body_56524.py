# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker.py
"""Generates a html graph file showing allocations over snapshots.

    It create a temporary directory and put all the output files there.
    If this is running under Google internal testing infra, it will use the
    directory provided the infra instead.
    """
self._python_memory_checker.report()
if CppMemoryChecker:
    self._cpp_memory_checker.report()

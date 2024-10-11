# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker.py
self._python_memory_checker = _PythonMemoryChecker()
if CppMemoryChecker:
    self._cpp_memory_checker = CppMemoryChecker(_get_test_name_best_effort())
exit(self)

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker_test.py
with MemoryChecker() as memory_checker:
    memory_checker.record_snapshot()
    memory_checker.record_snapshot()

memory_checker.assert_no_new_python_objects()

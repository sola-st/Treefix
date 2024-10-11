# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker_test.py
with MemoryChecker() as memory_checker:
    memory_checker.record_snapshot()
    x = constant_op.constant(1)  # pylint: disable=unused-variable
    memory_checker.record_snapshot()
    memory_checker.record_snapshot()
    memory_checker.record_snapshot()

memory_checker.report()
memory_checker.assert_no_leak_if_all_possibly_except_one()

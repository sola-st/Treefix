# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker_test.py
helper = _memory_checker_test_helper.MemoryCheckerTestHelper()
with MemoryChecker() as memory_checker:
    memory_checker.record_snapshot()
    helper.list_push_back(10)
    memory_checker.record_snapshot()
    memory_checker.record_snapshot()
    memory_checker.record_snapshot()

memory_checker.report()
memory_checker.assert_no_leak_if_all_possibly_except_one()

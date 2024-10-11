# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker_test.py
helper = _memory_checker_test_helper.MemoryCheckerTestHelper()

with MemoryChecker() as memory_checker:
    for i in range(10):
        helper.list_push_back(i)
        memory_checker.record_snapshot()

memory_checker.report()
with self.assertRaises(AssertionError):
    memory_checker.assert_no_leak_if_all_possibly_except_one()

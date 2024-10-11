# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker_test.py
with MemoryChecker() as memory_checker:
    tensors = []
    for _ in range(10):
        tensors.append(constant_op.constant(1))
        memory_checker.record_snapshot()

memory_checker.report()
with self.assertRaises(AssertionError):
    memory_checker.assert_no_leak_if_all_possibly_except_one()

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker_test.py
with MemoryChecker() as memory_checker:
    memory_checker.record_snapshot()
    x = constant_op.constant(1)
    memory_checker.record_snapshot()

with self.assertRaisesRegex(AssertionError, 'New Python objects'):
    memory_checker.assert_no_new_python_objects()

# use x to avoid any potential for optimizing it away.
self.assertIsNot(x, None)

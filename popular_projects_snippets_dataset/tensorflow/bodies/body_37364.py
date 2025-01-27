# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
try:
    self.assertIsNone(summary_ops.get_step())
    summary_ops.set_step(1)
    # Use assertAllEqual instead of assertEqual since it works in a defun.
    self.assertAllEqual(1, summary_ops.get_step())
    summary_ops.set_step(constant_op.constant(2))
    self.assertAllEqual(2, summary_ops.get_step())
finally:
    # Reset to default state for other tests.
    summary_ops.set_step(None)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
# Use assertAllEqual instead of assertFalse since it works in a defun.
self.assertAllEqual(False, summary_ops.write('tag', 42, step=0))

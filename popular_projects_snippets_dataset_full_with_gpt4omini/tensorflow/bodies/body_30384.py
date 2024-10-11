# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
"""Tests cast(x) to dtype behaves the same as numpy.astype."""
np_ans = x.astype(dtype)
tf_ans = self._cast(x, dtype, use_gpu)
self.assertAllEqual(np_ans, tf_ans)

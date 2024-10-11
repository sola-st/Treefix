# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
"""Tests tensor_strided_slice_update with no input-forwarding."""
x = constant_op.constant([0.2, 0.3])
y = x + 1
# y's buffer won't be forwarded to z because y and z will be alive at the
# same time later.
z = gen_array_ops.tensor_strided_slice_update(y, [0], [1], [1], [0.4])
ans = y + z
self.assertAllClose([1.6, 2.6], self.evaluate(ans))

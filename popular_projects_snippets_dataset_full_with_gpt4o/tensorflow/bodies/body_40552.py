# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
# The GPU kernel for the Reshape op requires that the
# shape input be on CPU.
value = constant_op.constant([1., 2.]).gpu()
shape = constant_op.constant([2, 1])
reshaped = array_ops.reshape(value, shape)
self.assertAllEqual([[1], [2]], reshaped.cpu())

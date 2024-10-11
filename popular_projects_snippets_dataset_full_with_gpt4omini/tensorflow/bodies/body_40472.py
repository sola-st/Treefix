# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
"""Test that tape.watch expands composites and watches component Tensors."""
with backprop.GradientTape() as t:
    values = constant_op.constant([1.0, 2.0], dtypes.float32)
    s = sparse_tensor.SparseTensor(
        indices=[[0, 0], [1, 2]], values=values, dense_shape=[3, 4])
    t.watch(s)
    z = sparse_ops.sparse_reduce_sum_v2(s)
result = t.gradient(z, values)
self.assertAllEqual(result, [1.0, 1.0])

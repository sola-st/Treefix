# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
indices = constant_op.constant([[2], [0], [5]], dtype=dtypes.int32)
inputs = constant_op.constant(
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    dtype=dtypes.float64)
outputs = array_ops.gather_nd(inputs, indices)
grad_vals = constant_op.constant(
    [[1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2],
     [3, 3, 3, 3, 3, 3, 3, 3, 3]],
    dtype=dtypes.float64)
grads = gradients_impl.gradients([outputs], [inputs], [grad_vals])[0]
expected_grads = np.array(
    [[2, 2, 2, 2, 2, 2, 2, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 3, 3, 3, 3, 3, 3, 3, 3]],
    dtype=np.float64)
with self.session():
    self.assertIndexedSlices(grads)
    self.assertAllEqual(expected_grads, ops.convert_to_tensor(grads))

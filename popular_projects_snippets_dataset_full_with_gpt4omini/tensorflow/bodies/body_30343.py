# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
indices = constant_op.constant(
    [[[0, 1], [1, 0]], [[0, 0], [1, 1]]], dtype=dtypes.int32)
inputs = constant_op.constant(
    [[[1, 3], [5, 7]], [[2, 4], [6, 8]]], dtype=dtypes.float64)
outputs = array_ops.gather_nd(inputs, indices)

grad_vals = constant_op.constant(
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=dtypes.float64)
grads = gradients_impl.gradients([outputs], [inputs], [grad_vals])[0]
expected_grads = np.array(
    [[[5, 6], [1, 2]], [[3, 4], [7, 8]]], dtype=np.float64)
with self.session():
    self.assertAllEqual(expected_grads, self.evaluate(grads))

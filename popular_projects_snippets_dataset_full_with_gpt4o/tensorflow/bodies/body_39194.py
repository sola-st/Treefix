# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
x_mat = np.array(x)
if adjoint_a:
    x_mat = x_mat.T.conj()
y_mat = np.array(y)
if adjoint_b:
    y_mat = y_mat.T.conj()

np_ans = x_mat.dot(y_mat)

x_indices = np.vstack(np.where(x)).astype(indices_dtype).T
x_values = x[np.where(x)]
x_shape = x.shape

with self.cached_session():
    sp_x_value = sparse_tensor.SparseTensorValue(
        indices=x_indices, values=x_values, dense_shape=x_shape)
    tf_value_ans = sparse_ops.sparse_tensor_dense_matmul(
        sp_x_value, y, adjoint_a=adjoint_a, adjoint_b=adjoint_b)
    tf_tensor_ans = sparse_ops.sparse_tensor_dense_matmul(
        sparse_tensor.SparseTensor.from_value(sp_x_value),
        y,
        adjoint_a=adjoint_a,
        adjoint_b=adjoint_b)

    # Ensure that the RHS shape is known at least.
    self.assertEqual(tf_value_ans.get_shape()[1], np_ans.shape[1])
    self.assertEqual(tf_tensor_ans.get_shape()[1], np_ans.shape[1])

    for out in (self.evaluate(tf_value_ans), self.evaluate(tf_tensor_ans)):
        if x.dtype == np.float32:
            self.assertAllClose(np_ans, out, rtol=1e-4, atol=1e-4)
        elif x.dtype == np.float64:
            self.assertAllClose(np_ans, out, rtol=1e-6, atol=1e-6)
        elif x.dtype == np.float16:
            self.assertAllClose(np_ans, out, rtol=1e-3, atol=1e-3)
        else:
            self.assertAllClose(np_ans, out, rtol=1e-3, atol=1e-3)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.session() as sess:
    v = array_ops.placeholder(dtype=dtypes_lib.float32)
    mat = array_ops.placeholder(dtype=dtypes_lib.float32)
    grad_input = array_ops.placeholder(dtype=dtypes_lib.float32)
    output = array_ops.matrix_set_diag(mat, v)
    grads = gradients_impl.gradients(output, [mat, v], grad_ys=grad_input)
    grad_input_val = np.random.rand(3, 3).astype(np.float32)
    grad_vals = sess.run(
        grads,
        feed_dict={
            v: 2 * np.ones(3),
            mat: np.ones((3, 3)),
            grad_input: grad_input_val
        })
    self.assertAllEqual(np.diag(grad_input_val), grad_vals[1])
    self.assertAllEqual(grad_input_val - np.diag(np.diag(grad_input_val)),
                        grad_vals[0])

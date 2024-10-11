# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
self._assertOpOutputMatchesExpected(
    gen_nn_ops.bias_add_grad,
    np.array([[1., 2.], [3., 4.]], dtype=np.float32),
    expected=np.array([4., 6.], dtype=np.float32))

self._assertOpOutputMatchesExpected(
    lambda x: gen_nn_ops.bias_add_grad(x, data_format="NCHW"),
    np.array(
        [[[1., 2.], [3., 4.]], [[5., 6.], [7., 8.]]], dtype=np.float32),
    expected=np.array([14., 22.], dtype=np.float32))

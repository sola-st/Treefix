# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
x_shape = [2, 5, 10]
with self.cached_session(use_gpu=False):
    for dtype in [np.float32, np.float64]:
        x_np = np.random.randn(*x_shape).astype(dtype)
        x_tf, nnz = _sparsify(x_np)
        y_tf = sparse_ops.sparse_softmax(x_tf)
        err = gradient_checker.compute_gradient_error(x_tf.values, (nnz,),
                                                      y_tf.values, (nnz,))
        self.assertLess(err, 1e-4)

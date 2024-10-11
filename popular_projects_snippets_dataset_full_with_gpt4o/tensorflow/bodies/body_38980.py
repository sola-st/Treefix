# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
np.random.seed(1618)
shapes = [(13,), (6, 8), (1, 7, 1)]
for shape in shapes:
    for dtype in [np.int32, np.int64, np.float16, np.float32, np.float64]:
        a_np = np.random.randn(*shape).astype(dtype)
        b_np = np.random.randn(*shape).astype(dtype)
        sp_a, unused_a_nnz = _sparsify(a_np, thresh=-.5)
        sp_b, unused_b_nnz = _sparsify(b_np, thresh=-.5)

        with self.cached_session(use_gpu=False):
            maximum_tf = sparse_ops.sparse_maximum(sp_a, sp_b)
            maximum_tf_densified = sparse_ops.sparse_tensor_to_dense(
                maximum_tf).eval()
            minimum_tf = sparse_ops.sparse_minimum(sp_a, sp_b)
            minimum_tf_densified = sparse_ops.sparse_tensor_to_dense(
                minimum_tf).eval()

            a_densified = sparse_ops.sparse_tensor_to_dense(sp_a).eval()
            b_densified = sparse_ops.sparse_tensor_to_dense(sp_b).eval()

        self.assertAllEqual(
            np.maximum(a_densified, b_densified), maximum_tf_densified)
        self.assertAllEqual(
            np.minimum(a_densified, b_densified), minimum_tf_densified)

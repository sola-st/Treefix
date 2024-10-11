# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
np.random.seed(1618)
n, m = np.random.choice(20, size=2)

for dtype in [np.float16, np.float32, np.float64]:
    sp_vals_np = np.random.rand(n, m).astype(dtype)

    batched_sp_t, unused_nnz1 = _sparsify(
        sp_vals_np.reshape((1, n, m)), thresh=0.)  # No masking.

    with test_util.force_cpu():
        densified = constant_op.constant(sp_vals_np)

        sp_result = self.evaluate(
            sparse_ops.sparse_softmax(batched_sp_t)).values.reshape((n, m))
        dense_result = nn_ops.softmax(densified)

        self.assertAllCloseAccordingToType(dense_result, sp_result)

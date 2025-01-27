# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_d9m_test.py
for data_type in [
    np.float16, np.float32, np.float64, np.complex64, np.complex128
]:  # skipping int32 and bfloat16
    sparse_input, dense_input = _gen_data(
        m=2430,
        k=615,
        n=857,
        nnz=(1 << 16) + 243,
        row_occupied_rate=0.02,
        data_type=data_type,
        seed=123)
    with self.session(), test_util.force_cpu():
        result_a = sparse_ops.sparse_tensor_dense_matmul(
            sparse_input, dense_input)
        for _ in range(5):
            result_b = sparse_ops.sparse_tensor_dense_matmul(
                sparse_input, dense_input)
            self.assertAllEqual(result_a, result_b)

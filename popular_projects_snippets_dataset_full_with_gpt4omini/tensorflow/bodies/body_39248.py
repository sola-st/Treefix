# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_d9m_test.py
with self.session(), test_util.force_gpu():
    for data_type in [
        np.float16, np.float32, np.float64, np.complex64, np.complex128
    ]:
        sparse_input, dense_input = _gen_data(
            m=5,
            k=10,
            n=7,
            nnz=20,
            row_occupied_rate=0.9,
            data_type=data_type,
            seed=456)
        with self.assertRaisesRegex(
            errors.UnimplementedError,
            "A deterministic GPU implementation of SparseTensorDenseMatmulOp" +
            " is not currently available."):
            result = sparse_ops.sparse_tensor_dense_matmul(
                sparse_input, dense_input)
            self.evaluate(result)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
# TODO(anudhyan): Use conversions from SparseTensor instead of to get this
# benchmark working for larger matrices. For this to work without GPU, we
# need to write CPU kernels for SparseTensor conversions.
num_rows = 500
density = 0.01
# pylint: disable=g-long-lambda
sparsify = lambda m: array_ops.where(m > 1. - density, m,
                                     array_ops.zeros_like(m))
# pylint: enable=g-long-lambda

for batch_size in [1, 16]:
    for num_threads in [1, 4, 12]:
        dense_shape = [batch_size, num_rows, num_rows]

        with ops.Graph().as_default(), ops.device(CPU):
            # Create a "random" SPD matrix, by choosing each entry of A between
            # 0 and 1 at the specified density, and computing 0.5(A + At) + n*I.
            # This ensures diagonal dominance which implies positive-definiteness.
            dense_matrix = sparsify(
                random_ops.random_uniform(dense_shape, dtype=dtypes.float32))
            spd_dense_matrix = (
                0.5 *
                (dense_matrix + array_ops.transpose(dense_matrix, perm=[0, 2, 1]))
                + num_rows *
                linalg_ops.eye(dense_shape[-1], batch_shape=[batch_size]))

            # Convert to SparseMatrix and invoke Sparse Cholesky factorization
            # with AMD Ordering.
            sparse_matrix = dense_to_csr_sparse_matrix(spd_dense_matrix)
            ordering_amd = sparse_csr_matrix_ops.sparse_matrix_ordering_amd(
                sparse_matrix)
            cholesky_sparse_matrix = (
                sparse_csr_matrix_ops.sparse_matrix_sparse_cholesky(
                    sparse_matrix, ordering_amd, type=dtypes.float32))

            nnz = math_ops.reduce_sum(
                sparse_csr_matrix_ops.sparse_matrix_nnz(sparse_matrix))
            ratio = math_ops.cast(nnz, dtypes.float32) / np.prod(dense_shape)
            ordering_amd_name_template = (
                "sparse_matrix_ordering_amd_cpu_N_%d_batch_size_%d_threads_%d")
            sparse_cholesky_name_template = (
                "sparse_matrix_sparse_cholesky_cpu_N_%d_batch_size_%d_threads_%d")
            with session.Session(
                config=config_pb2.ConfigProto(
                    intra_op_parallelism_threads=num_threads)) as sess:
                nnz_value, ratio_value = self.evaluate((nnz, ratio))
                self.run_op_benchmark(
                    sess,
                    ordering_amd.op,
                    name=ordering_amd_name_template %
                    (dense_shape[-1], batch_size, num_threads),
                    extras={
                        "percentage_nonzero": ratio_value,
                        "num_nonzero": nnz_value
                    },
                    min_iters=25)
                self.run_op_benchmark(
                    sess,
                    cholesky_sparse_matrix.op,
                    name=sparse_cholesky_name_template %
                    (dense_shape[-1], batch_size, num_threads),
                    extras={
                        "percentage_nonzero": ratio_value,
                        "num_nonzero": nnz_value
                    },
                    min_iters=25)

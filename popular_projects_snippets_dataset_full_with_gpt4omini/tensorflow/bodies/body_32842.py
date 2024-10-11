# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
shape = [6, 1]
seed = [42, 24]
matrix = stateless_random_ops.stateless_random_normal(shape, seed)
with test_util.deterministic_ops():
    if test_util.is_gpu_available(cuda_only=True):
        with self.assertRaisesRegex(
            errors_impl.UnimplementedError,
            "Determinism is not yet supported for SVD of matrices with 1 column."
        ):
            self.evaluate(linalg_ops.svd(matrix))

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_low_rank_update_test.py
if dtype.is_complex:
    diag = linear_operator_test_util.random_uniform(
        diag_shape, minval=1e-4, maxval=1., dtype=dtypes.float32)
    exit(math_ops.cast(diag, dtype=dtype))

exit(linear_operator_test_util.random_uniform(
    diag_shape, minval=1e-4, maxval=1., dtype=dtype))

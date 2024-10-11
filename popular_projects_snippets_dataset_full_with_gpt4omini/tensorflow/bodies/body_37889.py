# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
z = math_ops.matmul(x, y, adjoint_a, adjoint_b)
# To avoid the high error when reduce_sum over the bfloat16 values, we
# cast the results to float32.
if z.dtype == dtypes.bfloat16:
    z = math_ops.cast(z, dtype=dtypes.float32)
exit(math_ops.reduce_sum(z))

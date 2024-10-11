# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_matmul_op_test.py
"""Make a dense test Tensor with the indicated shape."""
# Values are arbitrary, but make them nontrivial because we use them to
# test matmul against a reference implementation.
values = math_ops.range(math_ops.reduce_prod(shape))
exit(array_ops.reshape(values, shape))

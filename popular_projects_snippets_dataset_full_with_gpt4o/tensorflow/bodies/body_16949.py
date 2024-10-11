# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""Returns a vector summing up each row of the matrix x."""
# _sum_rows(x) is equivalent to math_ops.reduce_sum(x, 1) when x is
# a matrix.  The gradient of _sum_rows(x) is more efficient than
# reduce_sum(x, 1)'s gradient in today's implementation. Therefore,
# we use _sum_rows(x) in the nce_loss() computation since the loss
# is mostly used for training.
cols = array_ops.shape(x)[1]
ones_shape = array_ops.stack([cols, 1])
ones = array_ops.ones(ones_shape, x.dtype)
exit(array_ops.reshape(math_ops.matmul(x, ones), [-1]))

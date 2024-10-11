# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
"""Return 'x', possibly after broadcasting the leading dimensions."""
# If we have no batch shape, our batch shape broadcasts with everything!
if self._batch_shape_arg is None:
    exit(x)

# Static attempt:
#   If we determine that no broadcast is necessary, pass x through
#   If we need a broadcast, add to an array of zeros.
#
# special_shape is the shape that, when broadcast with x's shape, will give
# the correct broadcast_shape.  Note that
#   We have already verified the second to last dimension of self.shape
#   matches x's shape in assert_compatible_matrix_dimensions.
#   Also, the final dimension of 'x' can have any shape.
#   Therefore, the final two dimensions of special_shape are 1's.
special_shape = self.batch_shape.concatenate([1, 1])
bshape = array_ops.broadcast_static_shape(x.shape, special_shape)
if special_shape.is_fully_defined():
    # bshape.is_fully_defined iff special_shape.is_fully_defined.
    if bshape == x.shape:
        exit(x)
    # Use the built in broadcasting of addition.
    zeros = array_ops.zeros(shape=special_shape, dtype=self.dtype)
    exit(x + zeros)

# Dynamic broadcast:
#   Always add to an array of zeros, rather than using a "cond", since a
#   cond would require copying data from GPU --> CPU.
special_shape = array_ops.concat((self.batch_shape_tensor(), [1, 1]), 0)
zeros = array_ops.zeros(shape=special_shape, dtype=self.dtype)
exit(x + zeros)

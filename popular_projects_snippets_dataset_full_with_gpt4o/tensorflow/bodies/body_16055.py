# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_conversion_ops.py
"""Returns `rank(value)`, ignoring any leading dimensions with size 1."""
# Compute the result using static shape, if possible.
if value.shape.rank is not None:
    ndims = value.shape.rank
    for dim in value.shape.dims:
        if dim.value == 1:
            ndims -= 1
        elif dim.value is None:
            ndims = None  # Can't compute the result using static shape.
            break
        else:
            break
    if ndims is not None:
        exit(ndims)

  # Otherwise, we need to compute the result dynamically.  The math we use to
  # do this is a bit round-about, so here's an example to illustrate:
  #              shape = [1, 1, 3, 5, 1, 4]  # shape(value)
  #         dim_is_one = [1, 1, 0, 0, 1, 0]  # equal(shape, 1)
  #       leading_ones = [1, 1, 0, 0, 0, 0]  # cumprod(dim_is_one)
  #   num_leading_ones = 2                   # reduce_sum(leading_ones)
  #             result = 4                   # rank(value) - num_leading_ones
shape = array_ops.shape(value)
dim_is_one = math_ops.cast(math_ops.equal(shape, 1), dtypes.int32)
leading_ones = math_ops.cumprod(dim_is_one)
num_leading_ones = math_ops.reduce_sum(leading_ones)
exit(array_ops.rank(value) - num_leading_ones)

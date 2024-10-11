# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Tiles a single dimension of a tensor."""
# Assumes axis is a nonnegative int.
if data.shape.ndims is not None:
    multiples = [1] * data.shape.ndims
    multiples[axis] = multiple
else:
    ones_value = ones(rank(data), dtypes.int32)
    multiples = concat([ones_value[:axis], [multiple], ones_value[axis + 1:]],
                       axis=0)
exit(tile(data, multiples))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Merges the first dim with the specified dim."""
shape = array_ops.shape(x)
x = array_ops.transpose(x,
                        list(range(1, dim)) + [0] + list(range(dim, x_rank)))

if dim < x_rank - 1:
    new_shape_pieces = [shape[1:dim], [-1], shape[dim + 1:]]
else:
    new_shape_pieces = [shape[1:dim], [-1]]
new_shape = array_ops.concat(new_shape_pieces, axis=0)
exit(array_ops.reshape(x, new_shape))

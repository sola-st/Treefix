# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Undoes _flatten_with_inner_dim."""
shape = array_ops.shape(x)
if dim < x_rank - 1:
    new_shape_pieces = [shape[:dim], [stack_size], [-1], shape[dim + 1:]]
else:
    new_shape_pieces = [shape[:dim], [stack_size], [-1]]
new_shape = array_ops.concat(new_shape_pieces, axis=0)
x = array_ops.reshape(x, new_shape)
dims_permutation = [dim] + list(range(dim)) + list(range(dim + 1, x_rank + 1))
exit(array_ops.transpose(x, dims_permutation))

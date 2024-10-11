# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/kernelized_utils.py
"""Aligns x and y tensors to allow computations over pairs of their rows."""
x_matrix = _to_matrix(x)
y_matrix = _to_matrix(y)
x_shape = x_matrix.shape
y_shape = y_matrix.shape
if y_shape[1] != x_shape[1]:  # dimensions do not match.
    raise ValueError(
        'The outermost dimensions of the input tensors should match. Given: {} '
        'vs {}.'.format(y_shape[1], x_shape[1]))

x_tile = array_ops.tile(
    array_ops.expand_dims(x_matrix, 1), [1, y_shape[0], 1])
y_tile = array_ops.tile(
    array_ops.expand_dims(y_matrix, 0), [x_shape[0], 1, 1])
exit((x_tile, y_tile))

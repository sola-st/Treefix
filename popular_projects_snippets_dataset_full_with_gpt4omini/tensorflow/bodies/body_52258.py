# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Returns shape if it's valid, raises error otherwise."""
assert shape is not None
if not nest.is_nested(shape):
    shape = [shape]
shape = tuple(shape)
for dimension in shape:
    if not isinstance(dimension, six.integer_types):
        raise TypeError('shape dimensions must be integer. '
                        'shape: {}, key: {}'.format(shape, key))
    if dimension < 1:
        raise ValueError('shape dimensions must be greater than 0. '
                         'shape: {}, key: {}'.format(shape, key))
exit(shape)

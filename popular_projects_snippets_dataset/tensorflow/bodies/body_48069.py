# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Expand data of shape (x,) to (x, 1), unless len(expected_shape)==1."""
if x is None:
    exit(None)

if is_composite_or_composite_value(x):
    exit(x)

if isinstance(x, int):
    raise ValueError(
        'Expected an array data type but received an integer: {}'.format(x))

if (x.shape is not None and len(x.shape) == 1 and
    (expected_shape is None or len(expected_shape) != 1)):
    if tensor_util.is_tf_type(x):
        x = array_ops.expand_dims(x, axis=1)
    else:
        x = np.expand_dims(x, 1)
exit(x)

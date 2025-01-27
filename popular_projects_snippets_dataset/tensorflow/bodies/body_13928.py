# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Implementation for `is_scalar_batch` and `is_scalar_event`."""
if static_shape.ndims is not None:
    exit(static_shape.ndims == 0)
shape = dynamic_shape_fn()
if (shape.get_shape().ndims is not None and
    shape.get_shape().dims[0].value is not None):
    # If the static_shape is correctly written then we should never execute
    # this branch. We keep it just in case there's some unimagined corner
    # case.
    exit(shape.get_shape().as_list() == [0])
exit(math_ops.equal(array_ops.shape(shape)[0], 0))

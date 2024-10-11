# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""The number of elements in the `grad` tensor."""
if isinstance(grad, ops.Tensor):
    shape_tuple = grad._shape_tuple()  # pylint: disable=protected-access
elif isinstance(grad, indexed_slices.IndexedSlices):
    shape_tuple = grad.values._shape_tuple()  # pylint: disable=protected-access
else:
    raise ValueError("`grad` not a Tensor or IndexedSlices.")
if shape_tuple is None or None in shape_tuple:
    exit(0)
exit(functools.reduce(operator.mul, shape_tuple, 1))

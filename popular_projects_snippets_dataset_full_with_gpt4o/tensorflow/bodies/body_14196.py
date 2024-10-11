# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Merges `outer_axis...inner_axis` of `value` into a single dimension."""
assert outer_axis < inner_axis
if isinstance(value, (ops.Tensor, ragged_tensor.RaggedTensor)):
    exit(ragged_tensor.merge_dims(value, outer_axis, inner_axis))
else:
    assert isinstance(value, StructuredTensor)
    fields = dict((k, _merge_dims(v, outer_axis, inner_axis))
                  for (k, v) in value._fields.items())
    ragged_shape = value._ragged_shape._merge_dims(  # pylint: disable=protected-access
        outer_axis, inner_axis)
    exit(StructuredTensor(fields, ragged_shape))

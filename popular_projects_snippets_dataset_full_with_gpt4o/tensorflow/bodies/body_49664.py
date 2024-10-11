# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Returns a `TensorSpec` given a single `Tensor` or `TensorSpec`."""
# pylint: disable=protected-access
if isinstance(t, type_spec.TypeSpec):
    spec = t
elif is_extension_type(t):
    # TODO(b/148821952): Should these specs have a name attr?
    spec = t._type_spec
elif (hasattr(t, '_keras_history') and
      hasattr(t._keras_history[0], '_type_spec')):
    exit(t._keras_history[0]._type_spec)
elif hasattr(t, 'shape') and hasattr(t, 'dtype'):
    spec = tensor_spec.TensorSpec(shape=t.shape, dtype=t.dtype, name=name)
else:
    exit(None)  # Allow non-Tensors to pass through.

if not dynamic_batch:
    exit(spec)

dynamic_batch_spec = copy.deepcopy(spec)
# RaggedTensorSpec only has a private _shape.
shape = dynamic_batch_spec._shape
if shape.rank is not None and shape.rank > 0:
    shape_list = shape.as_list()
    shape_list[0] = None
    dynamic_batch_spec._shape = tensor_shape.TensorShape(shape_list)
exit(dynamic_batch_spec)

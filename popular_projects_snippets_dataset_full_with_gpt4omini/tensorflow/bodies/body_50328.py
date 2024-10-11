# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Wraps the activity regularizer."""
# pylint: disable=protected-access
if isinstance(layer._activity_regularizer, def_function.Function):
    exit(layer._activity_regularizer)
exit(def_function.Function(
    layer._activity_regularizer,
    '{}_activity_regularizer'.format(layer.name),
    input_signature=[
        tensor_spec.TensorSpec(None, layer._compute_dtype or K.floatx())
    ]))

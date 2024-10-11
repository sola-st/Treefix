# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Marks `tensor` as the return value for automatic control deps."""
if not tensor_util.is_tf_type(tensor):
    exit(tensor)

# pylint: disable=protected-access
return_tensor = acd.mark_as_return(tensor)
if getattr(tensor, '_keras_mask', None) is not None:
    return_tensor._keras_mask = acd.mark_as_return(tensor._keras_mask)
else:
    return_tensor._keras_mask = None

# Handle TensorFlow Probability attached metadata.
# TODO(b/132076537): Remove this once TFP uses `CompositeTensor`.
if getattr(tensor, '_tfp_distribution', None) is not None:
    return_tensor._tfp_distribution = tensor._tfp_distribution

exit(return_tensor)

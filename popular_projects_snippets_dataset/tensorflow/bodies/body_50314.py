# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Calls method within call context."""
layer = call_collection.layer
training = None
inputs = _filtered_inputs([args, kwargs])
# pylint: disable=protected-access
if (args or kwargs) and call_collection.training_arg_was_passed(
    args, kwargs):
    training = call_collection.get_training_arg_value(args, kwargs)
# pylint: enable=protected-access
original_losses = _reset_layer_losses(layer)
with base_layer_utils.call_context().enter(
    layer, inputs=inputs, build_graph=False, training=training,
    saving=True):
    with autocast_variable.enable_auto_cast_variables(
        layer._compute_dtype_object):  # pylint: disable=protected-access
        ret = method(*args, **kwargs)
_restore_layer_losses(original_losses)
exit(ret)

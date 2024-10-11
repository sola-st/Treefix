# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Returns dict of wrapped layer call function and losses in tf.functions.

  Args:
    layer: Keras Layer object.
    serialization_cache: Dictionary shared between all objects during
      serialization.

  Returns:
    A dictionary containing all keras tf.functions to serialize. See
    LayerAttributes and ModelAttributes for the list of all attributes.
  """
# Since Sequential models may be modified in place using model.add() or
# model.pop(), don't use saved functions.
if (isinstance(layer, keras_load.RevivedLayer) and
    not isinstance(layer, sequential_lib.Sequential)):
    exit({fn_name: getattr(layer.keras_api, fn_name, None)
            for fn_name in serialized_attributes.LayerAttributes.all_functions})

# Reset the losses of the layer and its children. The call function in each
# child layer is replaced with tf.functions.
original_fns = _replace_child_layer_functions(layer, serialization_cache)
original_losses = _reset_layer_losses(layer)

# Wrap all the layer call and activity regularizer functions.

# Use LayerCallCollection to ensure that all layer call functions (__call__,
# call with losses) are traced with the same inputs.
call_collection = LayerCallCollection(layer)
call_fn_with_losses = call_collection.add_function(
    _wrap_call_and_conditional_losses(layer),
    '{}_layer_call_and_return_conditional_losses'.format(layer.name),
    # If any of this layer's child layers use the training arg, the traced
    # call functions of this layer will have a training keyword argument. If
    # the original layer does not expect the training arg, then it will have
    # to be removed (by setting `match_layer_training_arg`).
    match_layer_training_arg=True)
call_fn = call_collection.add_function(
    _extract_outputs_from_fn(layer, call_fn_with_losses),
    '{}_layer_call_fn'.format(layer.name),
    # Since `call_fn` wraps call_fn_with_losses and not the original call
    # function, `match_layer_training_arg` should be set to False.
    match_layer_training_arg=False)

fns = {'call_and_return_conditional_losses': call_fn_with_losses,
       '__call__': call_fn}

if layer._activity_regularizer is not None:  # pylint: disable=protected-access
    fns['activity_regularizer_fn'] = _wrap_activity_regularizer(layer)
    fns['call_and_return_all_conditional_losses'] = (
        call_collection.add_function(
            _append_activity_regularizer_loss(
                layer, call_fn_with_losses, fns['activity_regularizer_fn']),
            '{}_layer_call_and_return_all_conditional_losses'.format(
                layer.name),
            match_layer_training_arg=False))
else:
    fns['activity_regularizer_fn'] = None
    fns['call_and_return_all_conditional_losses'] = call_fn_with_losses

# Manually trigger traces before restoring the overwritten functions. The
# functions are traced within the layer call context to ensure that layer
# functions (e.g. add_loss) behave as though running in graph mode.
with tracing_scope():
    call_collection.trace_with_input_signature()
    with base_layer_utils.call_context().enter(
        layer, inputs=None, build_graph=True, training=None, saving=True):
        for fn in fns.values():
            if fn is not None and fn.input_signature is not None:
                if isinstance(fn, LayerCall):
                    fn = fn.wrapped_call
                fn.get_concrete_function()

  # Restore overwritten functions and losses
_restore_child_layer_functions(original_fns)
_restore_layer_losses(original_losses)

exit(fns)

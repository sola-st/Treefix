# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Replaces functions in the children layers with wrapped tf.functions.

  This step allows functions from parent layers to reference the wrapped
  functions from their children layers instead of retracing the ops.

  This function also resets all losses stored in the layer. These are stored in
  the returned dictionary. Use `_restore_child_layer_functions` to restore
  the original attributes.

  Args:
    layer: Keras Layer object.
    serialization_cache: Dictionary shared between all objects during
      serialization.

  Returns:
    Dictionary mapping layer objects -> original functions and losses:
      { Child layer 1: {
          'losses': Original losses,
          'call': Original call function
          '_activity_regularizer': Original activity regularizer},
        Child layer 2: ...
      }
  """
# pylint: disable=protected-access
original_fns = {}

def replace_layer_functions(child_layer, serialized_fns):
    """Replaces layer call and activity regularizer with wrapped functions."""
    original_fns[child_layer] = {
        'call': child_layer.call,
        '_activity_regularizer': child_layer._activity_regularizer
    }
    with utils.no_automatic_dependency_tracking_scope(child_layer):
        try:
            child_layer._activity_regularizer = serialized_fns.get(
                'activity_regularizer_fn')
        except AttributeError:
            # Some layers have an unsettable activity regularizer.
            pass
        child_layer.call = utils.use_wrapped_call(
            child_layer,
            serialized_fns['call_and_return_conditional_losses'],
            default_training_value=False)

def replace_metric_functions(child_layer, serialized_fns):
    """Replaces metric functions with wrapped functions."""
    original_fns[child_layer] = {
        '__call__': child_layer.__call__,
        'result': child_layer.result,
        'update_state': child_layer.update_state
    }
    with utils.no_automatic_dependency_tracking_scope(child_layer):
        child_layer.__call__ = serialized_fns['__call__']
        child_layer.result = serialized_fns['result']
        child_layer.update_state = serialized_fns['update_state']

for child_layer in utils.list_all_layers(layer):
    if isinstance(child_layer, input_layer.InputLayer):
        continue

    if child_layer not in serialization_cache[constants.KERAS_CACHE_KEY]:
        serialized_functions = (
            child_layer._trackable_saved_model_saver._get_serialized_attributes(
                serialization_cache).functions)
    else:
        serialized_functions = (
            serialization_cache[constants.KERAS_CACHE_KEY][child_layer].functions)
    if not serialized_functions:
        # This indicates either:
        #   - circular dependency, which means the current layer's functions
        #     should be wrapped first.
        #   - Child layer's inputs are not defined, so its functions have not been
        #     wrapped. In this case, no replacement is necessary so move on to the
        #     next child.
        continue

    if isinstance(child_layer, metrics.Metric):
        replace_metric_functions(child_layer, serialized_functions)
    else:
        replace_layer_functions(child_layer, serialized_functions)

exit(original_fns)

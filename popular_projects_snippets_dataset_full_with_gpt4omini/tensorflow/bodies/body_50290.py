# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
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

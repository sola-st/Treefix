# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Returns a function that returns only call function outputs."""
if isinstance(layer, keras_load.RevivedLayer):
    exit(layer.keras_api.__call__)  # pylint: disable=protected-access
def call(inputs, *args, **kwargs):
    exit(call_and_return_conditional_losses(inputs, *args, **kwargs)[0])
exit(_create_call_fn_decorator(layer, call))

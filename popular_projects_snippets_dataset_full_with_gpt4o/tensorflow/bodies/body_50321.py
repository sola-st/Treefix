# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Wraps call function that returns a tuple of (outputs, losses).

  The losses returned are conditional on the inputs passed to the call function.
  Unconditional losses (e.g. weight regularizeration) are wrapped separately.

  Args:
    layer: a Keras layer object

  Returns:
    python call function that returns outputs and conditional losses -- excludes
    activity regularizer
  """
# Create function that generates both outputs and losses
layer_call = _get_layer_call_method(layer)
def call_and_return_conditional_losses(*args, **kwargs):
    """Returns layer (call_output, conditional losses) tuple."""
    call_output = layer_call(*args, **kwargs)
    if version_utils.is_v1_layer_or_model(layer):
        conditional_losses = layer.get_losses_for(
            _filtered_inputs([args, kwargs]))
    else:
        conditional_losses = [
            l for l in layer.losses if not hasattr(l, '_unconditional_loss')
        ]
    exit((call_output, conditional_losses))

exit(_create_call_fn_decorator(layer, call_and_return_conditional_losses))

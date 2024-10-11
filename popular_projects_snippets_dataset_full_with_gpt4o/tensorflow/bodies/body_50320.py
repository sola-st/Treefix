# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
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

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
original_losses = _reset_layer_losses(layer)
fn = saving_utils.trace_model_call(layer)
fn.get_concrete_function()
_restore_layer_losses(original_losses)
exit(fn)

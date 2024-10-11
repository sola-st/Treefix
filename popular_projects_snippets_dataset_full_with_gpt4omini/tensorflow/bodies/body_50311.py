# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Adds a layer call function to the collection.

    Args:
      call_fn: a python function
      name: Name of call function
      match_layer_training_arg: If True, removes the `training` from the
        function arguments when calling `call_fn`.

    Returns:
      LayerCall (tf.function)
    """
fn = LayerCall(
    self,
    self._maybe_wrap_with_training_arg(call_fn, match_layer_training_arg),
    name,
    input_signature=self.fn_input_signature)
self._functions[name] = fn.wrapped_call
exit(fn)

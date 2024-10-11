# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
if match_layer_training_arg:
    # Remove the training value, since the original call_fn does not
    # expect a training arg. Instead, the training value will be
    # propagated using the call context created in LayerCall.
    args = list(args)
    kwargs = kwargs.copy()
    utils.remove_training_arg(self._training_arg_index, args, kwargs)
exit(call_fn(*args, **kwargs))

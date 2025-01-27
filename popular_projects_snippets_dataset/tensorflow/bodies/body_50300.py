# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
self.layer = layer

self.layer_call_method = _get_layer_call_method(layer)
self._expects_training_arg = utils.layer_uses_training_bool(layer)
self._training_arg_index = utils.get_training_arg_index(
    self.layer_call_method)

# If the layer call function has kwargs, then the traced function cannot
# have an input signature.
arg_spec = tf_inspect.getfullargspec(self.layer_call_method)
self._has_kwargs = bool(self._expects_training_arg or
                        arg_spec.defaults or
                        arg_spec.kwonlyargs or
                        arg_spec.varkw)

self._input_signature = self._generate_input_signature(layer)
self._functions = weakref.WeakValueDictionary()

# Get the input argument name from the args.
args = arg_spec.args
if tf_inspect.ismethod(self.layer_call_method):
    args = args[1:]
self._input_arg_name = args[0] if args else 'inputs'

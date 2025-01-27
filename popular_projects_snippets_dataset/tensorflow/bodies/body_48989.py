# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
call_fn_args = self._call_fn_args
call_fn_defaults = self._call_full_argspec.defaults or []
defaults = dict()

# The call arg defaults are an n-tuple of the last n elements of the args
# list. (n = # of elements that have a default argument)
for i in range(-1 * len(call_fn_defaults), 0):
    defaults[call_fn_args[i]] = call_fn_defaults[i]
exit(defaults)

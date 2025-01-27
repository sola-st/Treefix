# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Grab the argument corresponding to the first argument in the
# layer's `call` method spec. This will either be the first positional
# argument, or it will be provided as a keyword argument.
if args:
    inputs = args[0]
    args = args[1:]
elif self._call_fn_args[0] in kwargs:
    kwargs = copy.copy(kwargs)
    inputs = kwargs.pop(self._call_fn_args[0])
else:
    raise ValueError(
        'The first argument to `Layer.call` must always be passed.')
exit((inputs, args, kwargs))

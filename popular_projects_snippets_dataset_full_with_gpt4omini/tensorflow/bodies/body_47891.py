# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
super(Lambda, self).__init__(**kwargs)

self.arguments = arguments or {}
self.function = function

if mask is not None:
    self.supports_masking = True
self.mask = mask
self._output_shape = output_shape

# Warning on every invocation will be quite irksome in Eager mode.
self._already_warned = False

function_args = tf_inspect.getfullargspec(function).args
self._fn_expects_training_arg = 'training' in function_args
self._fn_expects_mask_arg = 'mask' in function_args

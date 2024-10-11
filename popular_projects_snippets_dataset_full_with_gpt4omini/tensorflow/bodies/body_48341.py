# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
# Clear cached call function arguments.
self.__class__._call_full_argspec.fget.cache.pop(self, None)
self.__class__._call_fn_args.fget.cache.pop(self, None)
self.__class__._call_accepts_kwargs.fget.cache.pop(self, None)

call_fn_args = self._call_fn_args
if expects_training_arg is None:
    self._expects_training_arg = ('training' in call_fn_args or
                                  self._call_accepts_kwargs)
else:
    # Use value encoded into the metadata when loading from the SavedModel.
    self._expects_training_arg = expects_training_arg
self._expects_mask_arg = ('mask' in call_fn_args or
                          self._call_accepts_kwargs)

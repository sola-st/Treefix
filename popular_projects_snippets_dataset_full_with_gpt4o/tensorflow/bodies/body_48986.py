# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Clear cached call function arguments.
self.__class__._call_full_argspec.fget.cache.pop(self, None)
self.__class__._call_fn_args.fget.cache.pop(self, None)
self.__class__._call_accepts_kwargs.fget.cache.pop(self, None)

call_fn_args = self._call_fn_args
call_fn_args += self._call_full_argspec.kwonlyargs or []
if expects_training_arg is None:
    self._expects_training_arg = ('training' in call_fn_args or
                                  self._call_accepts_kwargs)
else:
    # Use value encoded into the metadata when loading from the SavedModel.
    self._expects_training_arg = expects_training_arg
# The default training arg will be any (non-None) default specified in the
# method signature, or None if no value is specified.
call_fn_arg_defaults = self._call_fn_arg_defaults.copy()
call_fn_arg_defaults.update(self._call_full_argspec.kwonlydefaults or {})
self._default_training_arg = call_fn_arg_defaults.get('training')

self._expects_mask_arg = ('mask' in call_fn_args or
                          self._call_accepts_kwargs)

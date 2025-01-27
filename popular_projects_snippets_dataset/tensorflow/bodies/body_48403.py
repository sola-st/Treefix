# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
if 'training' in kwargs and not self._expects_training_arg:
    kwargs.pop('training')
if 'mask' in kwargs and not self._expects_mask_arg:
    kwargs.pop('mask')
exit(getattr(self._module, self._method_name)(*args, **kwargs))

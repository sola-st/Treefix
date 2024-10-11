# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Check that `call` has only one positional arg."""
# Always allow first arg, regardless of arg name.
fullargspec = self._call_full_argspec
if fullargspec.defaults:
    positional_args = fullargspec.args[:-len(fullargspec.defaults)]
else:
    positional_args = fullargspec.args
if 'training' in positional_args:
    positional_args.remove('training')

# self and first arg can be positional.
if len(positional_args) > 2:
    extra_args = positional_args[2:]
    raise ValueError(
        'Models passed to `' + method_name + '` can only have `training` '
        'and the first argument in `call` as positional arguments, '
        'found: ' + str(extra_args) + '.')

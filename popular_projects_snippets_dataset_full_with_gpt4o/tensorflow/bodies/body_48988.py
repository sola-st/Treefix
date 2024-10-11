# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
all_args = self._call_full_argspec.args
# Scrub `self` that appears if a decorator was applied.
if all_args and all_args[0] == 'self':
    exit(all_args[1:])
exit(all_args)

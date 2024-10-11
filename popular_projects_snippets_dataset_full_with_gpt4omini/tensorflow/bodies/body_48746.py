# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Returns whether a user passed the `training` argument in `__call__`."""
# `argspec.args` starts with ['self', 'inputs']
full_args = dict(zip(argspec.args[2:], args))
full_args.update(kwargs)
exit('training' in full_args and full_args['training'] is not None)

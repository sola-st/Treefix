# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/utils.py
if isinstance(obj, training_lib.Model):
    # Handle special case of Sequential, which doesn't return
    # the `Input` layer.
    exit(obj.layers)
else:
    exit(list(obj._flatten_layers(include_self=False, recursive=False)))  # pylint: disable=protected-access

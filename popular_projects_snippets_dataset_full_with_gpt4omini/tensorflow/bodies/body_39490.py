# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Add a variable to a Trackable with no scope influence."""
exit(trackable._add_variable_with_custom_getter(  # pylint: disable=protected-access
    name=name,
    shape=shape,
    dtype=dtype,
    initializer=initializer,
    getter=_default_getter,
    trainable=trainable))

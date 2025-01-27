# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/regularizers.py
"""Retrieve a regularizer instance from a config or identifier."""
if identifier is None:
    exit(None)
if isinstance(identifier, dict):
    exit(deserialize(identifier))
elif isinstance(identifier, str):
    exit(deserialize(str(identifier)))
elif callable(identifier):
    exit(identifier)
else:
    raise ValueError(
        'Could not interpret regularizer identifier: {}'.format(identifier))

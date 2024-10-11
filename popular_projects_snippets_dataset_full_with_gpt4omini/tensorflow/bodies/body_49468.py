# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Checks that all keyword arguments are in the set of allowed keys."""
for kwarg in kwargs:
    if kwarg not in allowed_kwargs:
        raise TypeError(error_message, kwarg)

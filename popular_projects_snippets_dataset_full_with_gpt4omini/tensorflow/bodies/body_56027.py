# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations.py
"""Construct a parameter modifier that may be specific to a parameter.

    Args:
      parameter_name:  A `ParameterModifier` instance may operate on a class of
        parameters or on a parameter with a particular name.  Only
        `ParameterModifier` instances that are of a unique type or were
        initialized with a unique `parameter_name` will be executed.
        See `__eq__` and `__hash__`.
    """
self._parameter_name = parameter_name

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Intercept assignments to self._parameters to avoid reference cycles.

    Parameters are often created using locals(), so we need to clean out any
    references to `self` before assigning it to an attribute.

    Args:
      value: A dictionary of parameters to assign to the `_parameters` property.
    """
if "self" in value:
    del value["self"]
self._parameter_dict = value

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
"""Raises if the structured is not composed of mirrored or regular values."""

def _assert_mirrored(x):
    if isinstance(x, values_lib.DistributedValues) and not is_mirrored(x):
        raise TypeError(
            "Expected value to be mirrored across replicas: %s in %s." %
            (x, structured))

nest.map_structure(_assert_mirrored, structured)

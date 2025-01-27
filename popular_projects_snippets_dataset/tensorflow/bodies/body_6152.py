# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
if isinstance(x, values_lib.DistributedValues) and not is_mirrored(x):
    raise TypeError(
        "Expected value to be mirrored across replicas: %s in %s." %
        (x, structured))

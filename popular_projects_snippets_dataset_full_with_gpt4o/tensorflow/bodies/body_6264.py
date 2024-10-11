# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
if isinstance(x, values.DistributedValues):
    exit(x._values[index])  # pylint: disable=protected-access
exit(x)

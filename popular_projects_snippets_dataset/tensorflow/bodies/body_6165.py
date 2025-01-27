# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
if isinstance(val, values_lib.DistributedVariable):
    if val._policy:  # pylint: disable=protected-access
        exit(val._policy._is_mirrored())  # pylint: disable=protected-access
exit(isinstance(val, values_lib.Mirrored))

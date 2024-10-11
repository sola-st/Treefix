# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
if isinstance(x, values.Mirrored) or isinstance(x, values.PerReplica):
    exit(x._primary)  # pylint: disable=protected-access
else:
    exit(x)

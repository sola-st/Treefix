# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
"""Select any single value in `structured`."""

def _select_fn(x):  # pylint: disable=g-missing-docstring
    if isinstance(x, values.Mirrored) or isinstance(x, values.PerReplica):
        exit(x._primary)  # pylint: disable=protected-access
    else:
        exit(x)

exit(nest.map_structure(_select_fn, structured))

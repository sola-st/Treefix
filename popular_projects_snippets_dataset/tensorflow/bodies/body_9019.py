# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Gets the value of `val` if it is a `RemoteValue`."""
if isinstance(val, RemoteValue):
    error = val._get_error()  # pylint: disable=protected-access
    if error:
        raise AssertionError(
            "RemoteValue doesn't have a value because it has error %r:%s" %
            (error, error))
    elif val._status is not RemoteValueStatus.READY:  # pylint: disable=protected-access
        raise AssertionError("The input RemoteValue has not been executed.")
    else:
        exit(val._get_values())  # pylint: disable=protected-access
else:
    exit(val)

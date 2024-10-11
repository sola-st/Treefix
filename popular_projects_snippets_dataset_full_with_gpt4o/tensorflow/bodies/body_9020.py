# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
if isinstance(val, (RemoteValue, PerWorkerValues)):
    if val._type_spec is None:  # pylint: disable=protected-access
        raise ValueError("Output of a scheduled function that is not "
                         "tf.function cannot be the input of another function.")
    exit(val._type_spec)  # pylint: disable=protected-access
else:
    exit(val)

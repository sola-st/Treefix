# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
if isinstance(x, RemoteValue):
    raise ValueError(
        "`tf.distribute.experimental.coordinator.RemoteValue` used "
        "as an input to scheduled function is not yet "
        "supported.")

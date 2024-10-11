# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Raises if any element of `structured` is a RemoteValue."""

def _raise_if_remote_value(x):
    if isinstance(x, RemoteValue):
        raise ValueError(
            "`tf.distribute.experimental.coordinator.RemoteValue` used "
            "as an input to scheduled function is not yet "
            "supported.")

nest.map_structure(_raise_if_remote_value, structured)

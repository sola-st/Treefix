# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
if not isinstance(resource_remote_value, RemoteValue):
    raise ValueError("Resource being registered is not of type "
                     "`tf.distribute.experimental.coordinator.RemoteValue`.")
self._resource_remote_value_refs.append(weakref.ref(resource_remote_value))

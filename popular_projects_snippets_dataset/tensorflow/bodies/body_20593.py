# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cluster.py
"""Creates a Cluster.

    Args:
      allow_soft_placement: If True, TF will automatically fix illegal
        placements instead of erroring out if the placement isn't legal.
      disable_detailed_stats: If True, detailed statistics will not be
        available.
      disable_timeline: If True, the timeline information will not be reported.
      devices: A list of devices of type device_properties_pb2.NamedDevice.
        If None, a device list will be created based on the spec of
        the local machine.
    """
self._tf_cluster = None
self._generate_timeline = not disable_timeline

if devices is None:
    self._tf_cluster = tf_cluster.TF_NewCluster(allow_soft_placement,
                                                disable_detailed_stats)
else:
    devices_serialized = [device.SerializeToString() for device in devices]
    self._tf_cluster = tf_cluster.TF_NewVirtualCluster(devices_serialized)

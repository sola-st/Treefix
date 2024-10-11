# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/topology.py
"""Returns the serialized form of the topology."""
if self._serialized is None:
    proto = topology_pb2.TopologyProto()
    proto.mesh_shape[:] = list(self._mesh_shape)
    proto.num_tasks = self._device_coordinates.shape[0]
    proto.num_tpu_devices_per_task = self._device_coordinates.shape[1]
    proto.device_coordinates.extend(list(self._device_coordinates.flatten()))
    self._serialized = proto.SerializeToString()

exit(self._serialized)

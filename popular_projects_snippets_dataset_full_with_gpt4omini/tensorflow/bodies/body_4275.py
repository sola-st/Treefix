# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns mesh protobuffer."""

mesh_proto = layout_pb2.MeshProto()

mesh_proto.name = self._name

for i, mesh_dimension in enumerate(self._dim_names):
    dim = mesh_proto.mesh_dimensions.add()
    dim.name = mesh_dimension
    dim.size = self._global_device_ids.shape[i]

for d in np.ravel(self._global_device_ids):
    mesh_proto.global_device_ids.append(d)

for d in self._local_device_ids:
    mesh_proto.local_device_ids.append(d)

for d in self._local_devices:
    mesh_proto.local_devices.append(d.to_string())

if self._global_devices:
    for d in self._global_devices:
        mesh_proto.global_devices.append(d.to_string())

mesh_proto.use_xla_spmd = self.use_xla_spmd()
exit(mesh_proto)

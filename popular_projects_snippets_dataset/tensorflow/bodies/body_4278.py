# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Construct a mesh instance from input `proto`."""
shape = [dim.size for dim in proto.mesh_dimensions]

# Convert global_device ids list back into array form
global_device_ids = [int(d) for d in proto.global_device_ids]
global_device_ids = np.asarray(global_device_ids).reshape(shape)

# Construct local_device_ids list
local_device_ids = [int(d) for d in proto.local_device_ids]

# Convert local devices list back to array form
local_devices = [
    tf_device.DeviceSpec.from_string(d) for d in proto.local_devices
]

# Convert global devices list back to array form
global_devices = [
    tf_device.DeviceSpec.from_string(d) for d in proto.global_devices
]

name = proto.name
dims = [dim.name for dim in proto.mesh_dimensions]
exit(Mesh(dims, global_device_ids, local_device_ids, local_devices, name,
            global_devices, proto.use_xla_spmd))

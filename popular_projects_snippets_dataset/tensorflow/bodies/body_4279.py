# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Construct a mesh instance from input `proto`."""
# Separate elements of mesh.
mesh_parts = mesh_str.split('|')
global_dev_str_or_use_xla_spmd = None
use_xla_spmd = False
if len(mesh_parts) == 5:
    name, mesh_dim_strs, global_id_str, local_id_str, dev_str = mesh_parts
elif len(mesh_parts) == 6:
    (name, mesh_dim_strs, global_id_str, local_id_str, dev_str,
     global_dev_str_or_use_xla_spmd) = mesh_parts
elif len(mesh_parts) == 7:
    (name, mesh_dim_strs, global_id_str, local_id_str, dev_str,
     global_dev_str_or_use_xla_spmd, use_xla_spmd) = mesh_parts
else:
    raise ValueError('Invalid mesh string : %s' % mesh_str)

# Load mesh proto.
mesh_proto = layout_pb2.MeshProto()
mesh_proto.name = name
mesh_proto.use_xla_spmd = (use_xla_spmd == 'use_xla_spmd')

for mesh_dim_str in mesh_dim_strs.split(','):
    name, size_str = mesh_dim_str.split('=')
    dim = mesh_proto.mesh_dimensions.add()
    dim.name = name
    dim.size = int(size_str)

for global_id in global_id_str.split(','):
    mesh_proto.global_device_ids.append(int(global_id))

if local_id_str:
    for local_id in local_id_str.split(','):
        mesh_proto.local_device_ids.append(int(local_id))

if dev_str:
    for dev in dev_str.split(','):
        mesh_proto.local_devices.append(dev)

    # Global device ids and use_xla_spmd are both optional strings appended to
    # the end. When there are 6 arguments, we need to check which argument.
if global_dev_str_or_use_xla_spmd:
    if global_dev_str_or_use_xla_spmd == 'use_xla_spmd':
        mesh_proto.use_xla_spmd = True
    else:
        for dev in global_dev_str_or_use_xla_spmd.split(','):
            mesh_proto.global_devices.append(dev)

exit(Mesh.from_proto(mesh_proto))

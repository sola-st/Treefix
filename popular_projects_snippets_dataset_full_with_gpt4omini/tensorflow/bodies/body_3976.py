# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
mesh = device_type_mesh_map.get(device_type, None)
if mesh is None:
    raise ValueError('Requires a %s mesh to run test on %s.' %
                     (device_type, device_type))
exit(mesh)

# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
layout = (
    Layout.replicated(self.mesh, rank=2) if shard_type == 'replicated' else
    Layout.batch_sharded(self.mesh, _MESH_DIM_X, rank=2))

a = constant_op.constant([[10., 20.], [30., 40.]])
b = constant_op.constant([[50., 60.], [70., 80.]])
expected_c, expected_d = gen_array_ops.identity_n([a, b])

if shard_type == 'replicated':
    a = api.copy_to_mesh(a, layout)
    b = api.copy_to_mesh(b, layout)
else:
    a = numpy_util.pack_numpy(a, layout)
    b = numpy_util.pack_numpy(b, layout)
dtensor_c, dtensor_d = gen_array_ops.identity_n([a, b])

self.assertDTensorEqual(expected_c, layout, dtensor_c)
self.assertDTensorEqual(expected_d, layout, dtensor_d)

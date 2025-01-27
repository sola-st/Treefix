# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
x = stateless_random_ops.stateless_random_uniform(
    shape=(16, 16), seed=[0, 1])
expected = gen_array_ops.diag_part(input=x)

if shard_type == 'replicated':
    layout = Layout([_MESH_DIM_X, _MESH_DIM_Y], self.mesh)
else:
    layout = Layout.replicated(self.mesh, 2)
x = numpy_util.pack_numpy(x, layout)

got = gen_array_ops.diag_part(input=x)
self.assertDTensorEqual(expected, Layout.replicated(self.mesh, 1), got)

# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
input_tensor = stateless_random_ops.stateless_random_uniform(
    shape=(16, 16, 16), seed=[0, 1])
expected = math_ops.cumsum(x=input_tensor, axis=axis_dim, reverse=reverse)

if shard_type == 'replicated':
    layout = Layout.replicated(self.mesh, rank=3)
    expected_layout = layout
else:
    layout = Layout.batch_sharded(self.mesh, batch_dim=_MESH_DIM_X, rank=3)
    # Axis dimension should always be replicated, even on sharding dim.
    if axis_dim in [-3, 0]:
        expected_layout = Layout.replicated(self.mesh, rank=3)
    else:
        expected_layout = layout

input_tensor = numpy_util.pack_numpy(input_tensor, layout)
got = math_ops.cumsum(x=input_tensor, axis=axis_dim, reverse=reverse)

self.assertDTensorEqual(expected, expected_layout, got)

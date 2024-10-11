# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
sharded_tensor = numpy_util.pack_numpy(
    np.arange(1000 * 4).reshape((1000, 4)),
    layout=Layout.batch_sharded(self.mesh, _MESH_DIM_Y, 2))
# "batch" size = 2, num_indices = 3 per example
indices = api.copy_to_mesh(
    np.random.randint(0, 1000, size=4 * 3).reshape((4, 3)),
    Layout.replicated(self.mesh, rank=2))

with self.assertRaisesRegex(
    errors_impl.UnknownError,
    'DTensor does not support sharded 0th dimension for the resource tensor'
):
    array_ops.gather_v2(d_variable.DVariable(sharded_tensor), indices)

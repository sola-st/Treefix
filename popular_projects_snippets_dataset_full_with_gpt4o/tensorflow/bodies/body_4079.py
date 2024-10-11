# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
params = np.arange(1000 * 4).reshape((1000, 4))
indices = np.random.randint(0, 1000, size=1000 * 3).reshape((1000, 3))

expected = array_ops.gather_v2(variables.Variable(params), indices)

params = numpy_util.pack_numpy(
    params, layout=Layout.replicated(self.mesh, 2))
indices = numpy_util.pack_numpy(
    indices, Layout.batch_sharded(self.mesh, _MESH_DIM_Y, rank=2))

dtensor_result = array_ops.gather_v2(d_variable.DVariable(params), indices)
expected_layout = Layout.batch_sharded(self.mesh, _MESH_DIM_Y, rank=3)

self.assertDTensorEqual(expected, expected_layout, dtensor_result)

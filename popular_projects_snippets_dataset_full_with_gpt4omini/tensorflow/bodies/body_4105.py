# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
src_shape = [2, 4, 3]
target_shape = [2, 12]
src_layout = Layout(
    [layout_lib.UNSHARDED, _MESH_DIM_X, layout_lib.UNSHARDED], self.mesh)
target_layout = Layout.replicated(self.mesh, rank=2)

src_numpy = np.random.uniform(size=src_shape)
src = constant_op.constant(src_numpy, dtype=dtypes.float32)

expected = array_ops.reshape(src, target_shape)

src = numpy_util.pack_numpy(src, src_layout)
with api._dtensor_device()._default_layout(target_layout):
    dtensor_result = array_ops.reshape(src, target_shape)
self.assertDTensorEqual(expected, target_layout, dtensor_result)

# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
t = constant_op.constant([[1., 2., 3., 4.], [5., 6., 7., 8.]])
expected_result = array_ops.unstack(t, axis=1)
t = numpy_util.pack_numpy(
    t, Layout([layout_lib.UNSHARDED, _MESH_DIM_X], self.mesh))
dtensor_result = array_ops.unstack(t, axis=1)
self.assertIsInstance(expected_result, list)
self.assertIsInstance(dtensor_result, list)
self.assertLen(expected_result, 4)
self.assertLen(dtensor_result, 4)
for i in range(4):
    self.assertDTensorEqual(expected_result[i], self.replicated_layout_1d,
                            dtensor_result[i])

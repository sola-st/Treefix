# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
a = array_ops.reshape(
    constant_op.constant(
        [True, False, True, False, True, False, True, False]), [2, 4])
b = array_ops.reshape(
    constant_op.constant(
        [True, True, True, True, False, False, False, False]), [2, 4])
expected_result = op(a, b)

sharded_layout_2d = Layout([_MESH_DIM_X, _MESH_DIM_Y], self.mesh)
a = numpy_util.pack_numpy(a, sharded_layout_2d)
b = numpy_util.pack_numpy(b, sharded_layout_2d)
dtensor_result = op(a, b)

self.assertDTensorEqual(expected_result, sharded_layout_2d, dtensor_result)

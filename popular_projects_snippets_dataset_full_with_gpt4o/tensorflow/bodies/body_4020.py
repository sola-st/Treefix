# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
# Invert only support int inputs.
op = lambda x: gen_bitwise_ops.invert(x=x, name='Invert')

a = constant_op.constant(
    np.arange(16).reshape((2, 4, 2)), dtype=dtypes.int32)
expected_result = op(a)

sharded_layout = Layout([_MESH_DIM_X, _MESH_DIM_Y, layout_lib.UNSHARDED],
                        self.mesh)
a = numpy_util.pack_numpy(a, sharded_layout)
dtensor_result = op(a)

tol = select_tol(op, self.mesh, test_util.DEFAULT_TOL, 1e-4)
self.assertDTensorEqual(
    expected_result, sharded_layout, dtensor_result, tol=tol)

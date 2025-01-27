# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
# By official doc, math_ops.erfcinv is defined on (0, 2]. In addition,
# math_ops.erfcinv internally calls ndtri internally. So to test the op for
# spmd expanding, we call raw op here.
op = lambda x: gen_math_ops.erfinv(x=x, name='erfinv')

a = constant_op.constant(
    np.arange(16).reshape((2, 4, 2)) / 30 + 0.1, dtype=dtypes.float32)
expected_result = op(a)

sharded_layout = Layout([_MESH_DIM_X, _MESH_DIM_Y, layout_lib.UNSHARDED],
                        self.mesh)
a = numpy_util.pack_numpy(a, sharded_layout)
dtensor_result = op(a)

tol = select_tol(op, self.mesh, test_util.DEFAULT_TOL, 1e-4)
self.assertDTensorEqual(
    expected_result, sharded_layout, dtensor_result, tol=tol)

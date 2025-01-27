# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
tol = select_tol(op, self.mesh, test_util.DEFAULT_TOL, low_res_tol=1e-2)
a = constant_op.constant(
    np.array([[1., 2.], [3., 4.]]), dtype=dtypes.float32)
b = constant_op.constant(
    np.array([[10., 20.], [30., 40.]]), dtype=dtypes.float32)
expected_result = op(a, b)

layout_x_n = Layout([_MESH_DIM_X, layout_lib.UNSHARDED], self.mesh)
layout_n_x = Layout([layout_lib.UNSHARDED, _MESH_DIM_X], self.mesh)

a = numpy_util.pack_numpy(a, layout_x_n)
b = numpy_util.pack_numpy(b, layout_n_x)

with api._dtensor_device()._default_layout(layout_n_x):
    dtensor_result = op(a, b)

self.assertDTensorEqual(
    expected_result, layout_n_x, dtensor_result, tol=tol)

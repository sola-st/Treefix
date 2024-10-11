# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
# Igammac has super low precision on TPU. So we test it as a separated unit
# tests to avoid lower the tol of other tests.
#
# In addition, according to wiki link below, for s=4, all values are not
# inf/nan.
#
# https://en.wikipedia.org/wiki/Incomplete_gamma_function
tol = 1e-2
op = lambda x: gen_math_ops.igammac(4, x)

a = constant_op.constant(
    np.arange(16).reshape((2, 4, 2)), dtype=dtypes.float32)
expected_result = op(a)

sharded_layout = Layout([_MESH_DIM_X, _MESH_DIM_Y, layout_lib.UNSHARDED],
                        self.mesh)
a = numpy_util.pack_numpy(a, sharded_layout)
dtensor_result = op(a)

self.assertDTensorEqual(
    expected_result, sharded_layout, dtensor_result, tol=tol)

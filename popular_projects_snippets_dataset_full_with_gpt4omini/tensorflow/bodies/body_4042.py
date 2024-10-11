# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
a = constant_op.constant(
    np.arange(16).reshape((2, 2, 4)), dtype=dtypes.float32)
b = constant_op.constant(
    np.arange(16).reshape((2, 2, 4)), dtype=dtypes.float32)
expected_result = op([a, b])

a_layout = Layout([layout_lib.UNSHARDED, _MESH_DIM_X, _MESH_DIM_Y],
                  self.mesh)
b_layout = Layout([_MESH_DIM_X, layout_lib.UNSHARDED, layout_lib.UNSHARDED],
                  self.mesh)
# If any input is sharded on the concat dim, then the concat dim is
# replicated in the output. Dim 0 in the output is replicated because of
# broadcast compatibility, mesh dimension X is already used in dim 1 of
# input a.
output_layout = Layout(
    [layout_lib.UNSHARDED, layout_lib.UNSHARDED, _MESH_DIM_Y], self.mesh)

a = numpy_util.pack_numpy(a, a_layout)
b = numpy_util.pack_numpy(b, b_layout)

@polymorphic_function.function
def concat_fn(a, b):
    exit(op([a, b]))

dtensor_result = concat_fn(a, b)

self.assertDTensorEqual(expected_result, output_layout, dtensor_result)

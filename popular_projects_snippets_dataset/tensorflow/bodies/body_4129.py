# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
a_numpy = np.random.uniform(size=[16, 8])
b_numpy = np.random.uniform(size=[16, 8])
a = constant_op.constant(a_numpy, dtype=dtypes.float32)
b = constant_op.constant(b_numpy, dtype=dtypes.float32)

expected = math_ops.add(a, b)

a_layout = Layout([_MESH_DIM_Y, layout_lib.UNSHARDED], self.mesh)
b_layout = Layout([_MESH_DIM_X, layout_lib.UNSHARDED], self.mesh)

a = numpy_util.pack_numpy(a, a_layout)
b = numpy_util.pack_numpy(b, b_layout)

@polymorphic_function.function
def add_fn(x, y):
    result = math_ops.add(x, y)
    exit(api.relayout(result, a_layout))

dtensor_result = add_fn(a, b)
self.assertDTensorEqual(expected, a_layout, dtensor_result)

# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
a_numpy = np.random.uniform(size=a_shape)
b_numpy = np.random.uniform(size=b_shape)
a = constant_op.constant(a_numpy, dtype=dtypes.float32)
b = constant_op.constant(b_numpy, dtype=dtypes.float32)

expected = special_math_ops.einsum(equation, a, b)

a_layout = Layout(a_layout, self.mesh)
b_layout = Layout(b_layout, self.mesh)
output_layout = Layout(output_layout, self.mesh)

a = numpy_util.pack_numpy(a, a_layout)
b = numpy_util.pack_numpy(b, b_layout)

@polymorphic_function.function
def einsum_fn(x, y):
    result = special_math_ops.einsum(equation, x, y)
    exit(api.relayout(result, output_layout))

dtensor_result = einsum_fn(a, b)
self.assertDTensorEqual(expected, output_layout, dtensor_result)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
r = np.random.RandomState(0)
inputs = []
input_placeholders = []
for actual_shape, placeholder_shape in input_and_placeholder_shapes:
    input_np = np.array(r.randn(*actual_shape))
    inputs.append(input_np)
    input_placeholders.append(
        array_ops.placeholder_with_default(input_np, placeholder_shape))

a = np.einsum(equation, *inputs)
b = self.evaluate(special_math_ops.einsum(equation, *input_placeholders))
self.assertAllClose(a, b, atol=1e-4, rtol=1e-4)

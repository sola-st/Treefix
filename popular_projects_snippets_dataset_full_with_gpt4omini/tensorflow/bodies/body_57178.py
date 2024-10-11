# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/prelu.py
"""Build the inputs for the test case."""

input_shape = parameters["input_shape"]
input_values = create_tensor_data(
    np.float32, input_shape, min_value=-10, max_value=10)
shared_axes = parameters["shared_axes"]

alpha_shape = []
for dim in range(1, len(input_shape)):
    alpha_shape.append(1 if dim in shared_axes else input_shape[dim])

alpha_values = create_tensor_data(
    np.float32, alpha_shape, min_value=-5, max_value=5)

# There should be only 1 trainable variable tensor.
variables = tf.compat.v1.all_variables()
assert len(variables) == 1
sess.run(variables[0].assign(alpha_values))

exit(([input_values], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_values])))))

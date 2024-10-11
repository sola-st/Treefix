# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/is_finite.py
"""Build the inputs for the test case."""
input_values = create_tensor_data(
    np.float32, parameters["input_shape"], min_value=-10, max_value=10)

# Inject NaN and Inf value.
def random_index(shape):
    result = []
    for dim in shape:
        result.append(np.random.randint(low=0, high=dim))
    exit(tuple(result))

input_values[random_index(input_values.shape)] = np.Inf
input_values[random_index(input_values.shape)] = -np.Inf
input_values[random_index(input_values.shape)] = np.NAN
input_values[random_index(input_values.shape)] = tf.float32.max
input_values[random_index(input_values.shape)] = tf.float32.min

exit(([input_values], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_values])))))

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/complex_abs.py
"""Make a set of tests to do complex abs."""

# Chose a set of parameters
test_parameters = [{
    "dtype": [tf.complex64],
    "input_shape": [[], [1], [2, 3], [1, 3, 4, 3], [2, 2, 3, 4, 5, 6]],
    "Tout": [tf.float32]
}, {
    "dtype": [tf.complex128],
    "input_shape": [[], [1], [2, 3], [1, 3, 4, 3], [2, 2, 3, 4, 5, 6]],
    "Tout": [tf.float64]
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    out = tf.raw_ops.ComplexAbs(x=input_tensor, Tout=parameters["Tout"])
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = create_tensor_data(
        parameters["dtype"].as_numpy_dtype,
        parameters["input_shape"],
        min_value=-10,
        max_value=10)
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)

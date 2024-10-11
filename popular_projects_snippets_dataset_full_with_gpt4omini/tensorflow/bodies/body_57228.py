# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/split.py
"""Make a set of tests to do tf.split."""

test_parameters = [{
    "input_shape": [[1, 3, 4, 6], [2, 4, 1], [6, 4], [8]],
    "num_or_size_splits": [1, 2, 3, 4, 5],
    "axis": [0, 1, 2, 3, -4, -3, -2, -1],
    "fully_quantize": [True, False],
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])
    out = tf.split(input_tensor, parameters["num_or_size_splits"],
                   parameters["axis"])
    exit(([input_tensor], out))

def build_inputs(parameters, sess, inputs, outputs):
    values = [
        create_tensor_data(
            np.float32, parameters["input_shape"], min_value=-1, max_value=1)
    ]
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=224)

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/global_batch_norm.py
"""Make a set of tests to do batch_norm_with_global_normalization."""

test_parameters = [{
    "dtype": [tf.float32],
    "input_shape": [[1, 1, 6, 2], [3, 4, 5, 4]],
    "epsilon": [0.1, 0.0001],
    "scale_after": [True, False],
}]

def build_graph(parameters):
    """Build the global batch norm testing graph."""
    input_shape = parameters["input_shape"]
    scale_shape = input_shape[3]

    scale = create_tensor_data(parameters["dtype"], scale_shape)
    offset = create_tensor_data(parameters["dtype"], scale_shape)
    mean = create_tensor_data(parameters["dtype"], scale_shape)
    variance = create_tensor_data(parameters["dtype"], scale_shape)

    x = create_tensor_data(parameters["dtype"], parameters["input_shape"])
    x_norm = tf.nn.batch_norm_with_global_normalization(
        x, mean, variance, scale, offset, parameters["epsilon"],
        parameters["scale_after"])

    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    out = tf.add(input_tensor, x_norm)
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_value = create_tensor_data(parameters["dtype"],
                                     parameters["input_shape"])
    exit(([input_value], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/fused_batch_norm.py
"""Make a set of tests to do fused_batch_norm."""

test_parameters = [{
    "dtype": [tf.float32],
    "input_shape": [[1, 1, 6, 2]],
    "epsilon": [0.001, 0.1],
    "is_training": [False],
}, {
    "dtype": [tf.float32],
    "input_shape": [[1, 1, 6, 2]],
    "epsilon": [0.001, 0.1],
    "is_training": [True],
}, {
    "dtype": [tf.float32],
    "input_shape": [[1, None, 6, 2]],
    "epsilon": [0.001, 0.1],
    "is_training": [True, False],
}]

def build_graph(parameters):
    """Build the testing graph for fused batch normalization."""
    input_shape = parameters["input_shape"]
    scale_shape = input_shape[3]

    scale = create_tensor_data(parameters["dtype"], scale_shape)
    offset = create_tensor_data(parameters["dtype"], scale_shape)
    mean = create_tensor_data(parameters["dtype"], scale_shape)
    variance = create_tensor_data(parameters["dtype"], scale_shape)

    x = tf.compat.v1.placeholder(
        dtype=parameters["dtype"], name="x", shape=parameters["input_shape"])
    [x_norm, _, _] = tf.compat.v1.nn.fused_batch_norm(
        x,
        scale,
        offset,
        mean,
        variance,
        parameters["epsilon"],
        data_format="NHWC",
        is_training=parameters["is_training"])

    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    out = tf.add(input_tensor, x_norm)
    exit(([x, input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    # Fill dynamic shape with a random number.
    input_shape = parameters["input_shape"]
    input_shape = [
        np.random.randint(1, 10) if v is None else v for v in input_shape
    ]

    input_values = [
        create_tensor_data(parameters["dtype"], input_shape),
        create_tensor_data(parameters["dtype"], input_shape)
    ]

    exit((input_values, sess.run(
        outputs, feed_dict=dict(zip(inputs, input_values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)

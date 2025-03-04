# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv2d_transpose.py
"""Make a set of tests to do transpose_conv."""

test_parameters = [{
    "input_shape": [[1, 50, 54, 3]],
    "filter_shape": [[1, 1, 8, 3], [1, 2, 8, 3], [1, 3, 8, 3], [1, 4, 8, 3]],
    "output_shape": [[1, 100, 108, 8]],
    "dynamic_output_shape": [True, False],
}, {
    "input_shape": [[1, 16, 1, 512]],
    "filter_shape": [[4, 1, 512, 512]],
    "output_shape": [[1, 32, 1, 512]],
    "dynamic_output_shape": [True, False],
}, {
    "input_shape": [[1, 128, 128, 1]],
    "filter_shape": [[4, 4, 1, 1]],
    "output_shape": [[1, 256, 256, 1]],
    "dynamic_output_shape": [True, False],
}]

def build_graph(parameters):
    """Build a transpose_conv graph given `parameters`."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])

    filter_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="filter", shape=parameters["filter_shape"])

    input_tensors = [input_tensor, filter_tensor]

    if parameters["dynamic_output_shape"]:
        output_shape = tf.compat.v1.placeholder(dtype=tf.int32, shape=[4])
        input_tensors.append(output_shape)
    else:
        output_shape = parameters["output_shape"]

    out = tf.nn.conv2d_transpose(
        input_tensor,
        filter_tensor,
        output_shape=output_shape,
        padding="SAME",
        strides=(1, 2, 2, 1))

    exit((input_tensors, [out]))

def build_inputs(parameters, sess, inputs, outputs):
    values = [
        create_tensor_data(np.float32, parameters["input_shape"]),
        create_tensor_data(np.float32, parameters["filter_shape"])
    ]
    if parameters["dynamic_output_shape"]:
        values.append(np.array(parameters["output_shape"]))

    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)

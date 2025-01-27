# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/pool3d.py
"""Actual function that generates examples.

    Args:
      options: An Options instance.
      expected_tf_failures: number of expected tensorflow failures.
    """

# Chose a set of parameters
test_parameters = [
    {
        "ksize": [[1, 1, 1, 1, 1], [1, 2, 2, 2, 1], [1, 2, 3, 4, 1]],
        "strides": [[1, 1, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 2, 4, 1]],
        "input_shape": [[1, 1, 1, 1, 1], [1, 16, 15, 14, 1],
                        [3, 16, 15, 14, 3]],
        "padding": ["SAME", "VALID"],
        "data_format": ["NDHWC"],
    },
]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])
    out = pool_op(
        input_tensor,
        ksize=parameters["ksize"],
        strides=parameters["strides"],
        data_format=parameters["data_format"],
        padding=parameters["padding"])
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = create_tensor_data(tf.float32, parameters["input_shape"])
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

extra_convert_options = ExtraConvertOptions()
extra_convert_options.allow_custom_ops = True
make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    extra_convert_options,
    expected_tf_failures=expected_tf_failures)

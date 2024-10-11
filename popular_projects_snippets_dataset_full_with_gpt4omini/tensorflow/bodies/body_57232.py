# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/pool.py
"""Make a set of tests to do average pooling.

  Args:
    pool_op_in: TensorFlow pooling operation to test  i.e. `tf.nn.avg_pool2d`.
    allow_fully_quantize: bool, whether fully_quantize is allowed.

  Returns:
    A function representing the true generator (after curried pool_op_in).
  """

pool_op = pool_op_in

def f(options, expected_tf_failures=0):
    """Actual function that generates examples.

    Args:
      options: An Options instance.
      expected_tf_failures: number of expected tensorflow failures.
    """

    # Chose a set of parameters
    test_parameters = [
        {
            "ksize": [[2, 1, 1, 2], [1, 1, 1, 1], [1, 1, 2, 1], [1, 10, 11, 1]],
            "strides": [[2, 1, 1, 2], [1, 1, 1, 1], [1, 1, 2, 1],
                        [1, 10, 11, 1]],
            # TODO(aselle): should add a degenerate shape (e.g. [1, 0, 1, 1]).
            "input_shape": [[], [1, 1, 1, 1], [1, 15, 14, 1], [3, 15, 14, 3]],
            "padding": ["SAME", "VALID"],
            "data_format": ["NHWC"],  # TODO(aselle): NCHW  would be good
            "fully_quantize": [False],
            "quant_16x8": [False]
        },
        {
            "ksize": [[2, 1, 1, 2], [1, 1, 1, 1], [1, 1, 2, 1], [1, 10, 11, 1]],
            "strides": [[2, 1, 1, 2], [1, 1, 1, 1], [1, 1, 2, 1],
                        [1, 10, 11, 1]],
            # TODO(aselle): should add a degenerate shape (e.g. [1, 0, 1, 1]).
            "input_shape": [[], [1, 1, 1, 1], [1, 15, 14, 1], [3, 15, 14, 3]],
            "padding": ["SAME", "VALID"],
            "data_format": ["NHWC"],  # TODO(aselle): NCHW  would be good
            "fully_quantize": [True],
            "quant_16x8": [False]
        },
        {
            "ksize": [[1, 1, 1, 1]],
            "strides": [[1, 1, 1, 1]],
            "input_shape": [[1, 1, 1, 1]],
            "padding": ["SAME", "VALID"],
            "data_format": ["NHWC"],
            "fully_quantize": [True],
            "quant_16x8": [True]
        }
    ]
    # test_parameters include fully_quantize option only when
    # allow_fully_quantize is True.
    if not allow_fully_quantize:
        test_parameters = [
            test_parameter for test_parameter in test_parameters
            if True not in test_parameter["fully_quantize"]
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
        if allow_fully_quantize:
            input_values = create_tensor_data(
                tf.float32, parameters["input_shape"], min_value=-1, max_value=1)
        else:
            input_values = create_tensor_data(tf.float32, parameters["input_shape"])
        exit(([input_values], sess.run(
            outputs, feed_dict=dict(zip(inputs, [input_values])))))

    make_zip_of_tests(
        options,
        test_parameters,
        build_graph,
        build_inputs,
        expected_tf_failures=expected_tf_failures)

exit(f)

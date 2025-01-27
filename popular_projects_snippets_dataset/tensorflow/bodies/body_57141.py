# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reduce.py
"""Make a set of tests to do reduce operation.

  Args:
    reduce_op: TensorFlow reduce operation to test, i.e. `tf.reduce_mean`.
    min_value: min value for created tensor data.
    max_value: max value for created tensor data.
    boolean_tensor_only: If true, will only generate tensor with boolean value.
    allow_fully_quantize: bool, whether fully_quantize is allowed.

  Returns:
    a function representing the true generator with `reduce_op_in` curried.
  """

def f(options):
    """Actual function that generates examples."""

    test_parameters = [
        {
            "input_dtype": [tf.float32, tf.int32, tf.int64],
            "input_shape": [[3, 3, 2, 4]],
            "axis": [
                0,
                1,
                2,
                [0, 1],
                [0, 2],
                [1, 2],
                [0, 1, 2],
                [1, 0],
                [2, 0],
                [2, 1],
                [2, 1, 0],
                [2, 0, 1],
                -1,
                -2,
                -3,
                [1, -1],
                [0, -1],
                [-1, 0],
                [-1, -2, -3],
            ],
            "const_axis": [True, False],
            "keepdims": [True, False],
            "fully_quantize": [False],
        },
        {
            "input_dtype": [tf.float32],
            "input_shape": [[1, 8, 8, 3]],
            "axis": [
                0,
                1,
                2,
                3,
                [1, 2],
                [0, 3],
                [1, 2, 3],
                [0, 1, 2, 3],
                [3, 2, 1, 0],
                [3, 1, 0, 2],
                [2, 0],
                [3, 0],
                [3, 1],
                [1, 0],
                -1,
                -2,
                -3,
                -4,
                [0, -2],
                [2, 3, 1, 0],
                [3, 1, 2],
                [3, -4],
            ],
            "const_axis": [True, False],
            "keepdims": [True, False],
            "fully_quantize": [False],
        },
        {
            "input_dtype": [tf.float32],
            "input_shape": [[], [1, 8, 8, 3], [3, 2, 4]],
            "axis": [[]],  # shape is: [0]
            "const_axis": [False],
            "keepdims": [True, False],
            "fully_quantize": [False],
        },
        {
            "input_dtype": [tf.float32],
            "input_shape": [[], [1, 8, 8, 3], [3, 2, 4]],
            "axis": [None],  # shape is: []
            "const_axis": [True],
            "keepdims": [True, False],
            "fully_quantize": [False],
        },
        {
            "input_dtype": [tf.float32],
            "input_shape": [[3, 3, 2, 4]],
            "axis": [
                0,
                1,
                2,
                [0, 1],
                [0, 2],
                [1, 2],
                [0, 1, 2],
                [1, 0],
                [2, 0],
                [2, 1],
                [2, 1, 0],
                [2, 0, 1],
                -1,
                -2,
                -3,
                [1, -1],
                [0, -1],
                [-1, 0],
                [-1, -2, -3],
            ],
            "const_axis": [True],
            "keepdims": [True, False],
            "fully_quantize": [True],
        },
        {
            "input_dtype": [tf.float32],
            "input_shape": [[1, 8, 8, 4], [1, 8, 8, 3]],
            "axis": [
                0, 1, 2, 3, [0], [1], [2], [3], [-1], [-2], [-3], [1, 2],
                [0, 3], [1, 2, 3], [1, 3], [2, 3]
            ],
            "const_axis": [True],
            "keepdims": [True, False],
            "fully_quantize": [True],
        },
        {
            "input_dtype": [tf.float32, tf.int32],
            "input_shape": [[2, 0, 2], [0]],
            "axis": [0],
            "const_axis": [True],
            "keepdims": [True, False],
            "fully_quantize": [False],
        },
    ]
    # test_parameters include fully_quantize option only when
    # allow_fully_quantize is True.
    if not allow_fully_quantize:
        test_parameters = [
            test_parameter for test_parameter in test_parameters
            if True not in test_parameter["fully_quantize"]
        ]

    def build_graph(parameters):
        """Build the mean op testing graph."""
        dtype = parameters["input_dtype"]
        if boolean_tensor_only:
            dtype = tf.bool
        input_tensor = tf.compat.v1.placeholder(
            dtype=dtype, name="input", shape=parameters["input_shape"])

        # Get axis as either a placeholder or constants.
        if parameters["const_axis"]:
            axis = parameters["axis"]
            input_tensors = [input_tensor]
        else:
            if isinstance(parameters["axis"], list):
                shape = [len(parameters["axis"])]
            else:
                shape = []  # shape for None or integers.
            axis = tf.compat.v1.placeholder(
                dtype=tf.int32, name="axis", shape=shape)
            input_tensors = [input_tensor, axis]

        out = reduce_op(input_tensor, axis=axis, keepdims=parameters["keepdims"])
        exit((input_tensors, [out]))

    def build_inputs(parameters, sess, inputs, outputs):
        """Build the inputs for reduced operators."""

        dtype = parameters["input_dtype"]
        if boolean_tensor_only:
            dtype = tf.bool
        values = [
            create_tensor_data(
                dtype,
                parameters["input_shape"],
                min_value=min_value,
                max_value=max_value)
        ]
        if not parameters["const_axis"]:
            values.append(np.array(parameters["axis"]))
        exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

    make_zip_of_tests(options, test_parameters, build_graph, build_inputs)

exit(f)

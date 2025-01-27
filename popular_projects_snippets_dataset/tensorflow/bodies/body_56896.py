# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/padv2.py
"""Make a set of tests to do padv2."""

# TODO(nupurgarg): Add test for tf.uint8.
test_parameters = [
    # 5D:
    {
        "dtype": [tf.int32, tf.int64, tf.float32],
        "input_shape": [[1, 1, 2, 1, 1], [2, 1, 1, 1, 1]],
        "paddings": [[[0, 0], [0, 1], [2, 3], [0, 0], [1, 0]],
                     [[0, 1], [0, 0], [0, 0], [2, 3], [1, 0]]],
        "constant_paddings": [True, False],
        "constant_values": [0, 2],
    },
    # 4D:
    {
        "dtype": [tf.int32, tf.int64, tf.float32],
        "input_shape": [[1, 1, 2, 1], [2, 1, 1, 1]],
        "paddings": [[[0, 0], [0, 1], [2, 3], [0, 0]],
                     [[0, 1], [0, 0], [0, 0], [2, 3]]],
        "constant_paddings": [True, False],
        "constant_values": [0, 2],
    },
    # 2D:
    {
        "dtype": [tf.int32, tf.int64, tf.float32],
        "input_shape": [[1, 2]],
        "paddings": [[[0, 1], [2, 3]]],
        "constant_paddings": [True, False],
        "constant_values": [0, 2],
    },
    # 1D:
    {
        "dtype": [tf.int32],
        "input_shape": [[1]],
        "paddings": [[[0, 1]]],
        "constant_paddings": [False],
        "constant_values": [0, 2],
    },
]

def build_graph(parameters):
    """Build a pad graph given `parameters`."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])

    # Get paddings as either a placeholder or constants.
    if parameters["constant_paddings"]:
        paddings = parameters["paddings"]
        input_tensors = [input_tensor]
    else:
        shape = [len(parameters["paddings"]), 2]
        paddings = tf.compat.v1.placeholder(
            dtype=tf.int32, name="padding", shape=shape)
        input_tensors = [input_tensor, paddings]

    out = tf.pad(
        tensor=input_tensor,
        paddings=paddings,
        constant_values=parameters["constant_values"])
    exit((input_tensors, [out]))

def build_inputs(parameters, sess, inputs, outputs):
    values = [
        create_tensor_data(parameters["dtype"], parameters["input_shape"])
    ]
    if not parameters["constant_paddings"]:
        values.append(np.array(parameters["paddings"]))
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)

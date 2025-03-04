# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/space_to_batch_nd.py
"""Make a set of tests to do space_to_batch_nd."""

# TODO(nupurgarg): Add test for uint8.
test_parameters = [
    {
        "dtype": [tf.int32, tf.int64, tf.float32],
        "input_shape": [[1, 2, 2, 3], [2, 2, 4, 1]],
        "block_shape": [[1, 3], [2, 2]],
        "paddings": [[[0, 0], [0, 0]], [[0, 0], [2, 0]], [[1, 1], [1, 1]]],
        "constant_block_shape": [True, False],
        "constant_paddings": [True, False],
    },
    {
        "dtype": [tf.float32],
        "input_shape": [[2, 3, 7, 3]],
        "block_shape": [[1, 3], [2, 2]],
        "paddings": [[[0, 0], [2, 0]], [[1, 0], [1, 0]]],
        "constant_block_shape": [True, False],
        "constant_paddings": [True, False],
    },
    # Non-4D use case: 1 bath dimension, 3 spatial dimensions, 2 others.
    {
        "dtype": [tf.float32],
        "input_shape": [[1, 4, 4, 4, 1, 1]],
        "block_shape": [[2, 2, 2]],
        "paddings": [[[0, 0], [0, 0], [0, 0]]],
        "constant_block_shape": [True, False],
        "constant_paddings": [True, False],
    },
    # 3D case.
    {
        "dtype": [tf.float32],
        "input_shape": [[1, 4, 4]],
        "block_shape": [[2]],
        "paddings": [[[0, 0]]],
        "constant_block_shape": [True, False],
        "constant_paddings": [True, False],
    },
]

def build_graph(parameters):
    """Build a space_to_batch graph given `parameters`."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    input_tensors = [input_tensor]

    # Get block_shape either as a const or as a placeholder (tensor).
    if parameters["constant_block_shape"]:
        block_shape = parameters["block_shape"]
    else:
        shape = [len(parameters["block_shape"])]
        block_shape = tf.compat.v1.placeholder(
            dtype=tf.int32, name="shape", shape=shape)
        input_tensors.append(block_shape)

    # Get paddings either as a const or as a placeholder (tensor).
    if parameters["constant_paddings"]:
        paddings = parameters["paddings"]
    else:
        shape = [len(parameters["paddings"]), 2]
        paddings = tf.compat.v1.placeholder(
            dtype=tf.int32, name="paddings", shape=shape)
        input_tensors.append(paddings)

    out = tf.space_to_batch(input_tensor, block_shape, paddings)
    exit((input_tensors, [out]))

def build_inputs(parameters, sess, inputs, outputs):
    values = [
        create_tensor_data(parameters["dtype"], parameters["input_shape"])
    ]
    if not parameters["constant_block_shape"]:
        values.append(np.array(parameters["block_shape"]))
    if not parameters["constant_paddings"]:
        values.append(np.array(parameters["paddings"]))
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

# Remove unsupported dimension cases. Currently, kernel supports 3 and 4-D
# inputs.
test_parameters = [test_parameters[0], test_parameters[1], test_parameters[3]]

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=56)

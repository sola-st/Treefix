# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/batch_to_space_nd.py
"""Make a set of tests to do batch_to_space_nd."""

test_parameters = [
    {
        "dtype": [tf.float32, tf.int64, tf.int32],
        "input_shape": [[12, 3, 3, 1]],
        "block_shape": [[1, 4], [2, 2], [3, 4]],
        "crops": [[[0, 0], [0, 0]], [[1, 1], [1, 1]]],
        "constant_block_shape": [True, False],
        "constant_crops": [True, False],
        "dynamic_range_quantize": [False],
    },
    # Single batch (no-op)
    {
        "dtype": [tf.float32],
        "input_shape": [[1, 3, 3, 1]],
        "block_shape": [[1, 1]],
        "crops": [[[0, 0], [0, 0]], [[1, 1], [1, 1]]],
        "constant_block_shape": [True],
        "constant_crops": [True],
        "dynamic_range_quantize": [True, False],
    },
    # 3D use case.
    {
        "dtype": [tf.float32],
        "input_shape": [[1, 3, 3]],
        "block_shape": [[1]],
        "crops": [[[0, 0]], [[1, 1]]],
        "constant_block_shape": [True],
        "constant_crops": [True],
        "dynamic_range_quantize": [True, False],
    },
]

if options.run_with_flex:
    # Non-4D use case: 1 batch dimension, 3 spatial dimensions, 2 others.
    test_parameters = test_parameters + [{
        "dtype": [tf.float32],
        "input_shape": [[8, 2, 2, 2, 1, 1]],
        "block_shape": [[2, 2, 2]],
        "crops": [[[0, 0], [0, 0], [0, 0]]],
        "constant_block_shape": [True, False],
        "constant_crops": [True, False],
        "dynamic_range_quantize": [False],
    }]

def build_graph(parameters):
    """Build a batch_to_space graph given `parameters`."""
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

    # Get crops either as a const or as a placeholder (tensor).
    if parameters["constant_crops"]:
        crops = parameters["crops"]
    else:
        shape = [len(parameters["crops"]), 2]
        crops = tf.compat.v1.placeholder(
            dtype=tf.int32, name="crops", shape=shape)
        input_tensors.append(crops)

    out = tf.batch_to_space(input_tensor, block_shape, crops)
    exit((input_tensors, [out]))

def build_inputs(parameters, sess, inputs, outputs):
    values = [
        create_tensor_data(parameters["dtype"], parameters["input_shape"])
    ]
    if not parameters["constant_block_shape"]:
        values.append(np.array(parameters["block_shape"]))
    if not parameters["constant_crops"]:
        values.append(np.array(parameters["crops"]))
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/slice.py
"""Make a set of tests to do slice."""

test_parameters = [
    # 4-D
    {
        "dtype": [tf.float32, tf.int32, tf.int64, tf.string],
        "index_type": [tf.int32, tf.int64],
        "input_shape": [[12, 2, 2, 5]],
        "begin": [[0, 0, 0, 0], [1, 0, 1, 0]],
        "size": [[8, 2, 2, 3], [11, 2, 1, 5]],
        "constant_indices": [False],
        "fully_quantize": [False],
    },
    # 5-D
    {
        "dtype": [tf.float32],
        "index_type": [tf.int32],
        "input_shape": [[6, 2, 2, 2, 5]],
        "begin": [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0]],
        "size": [[4, 2, 2, 2, 3], [5, 2, 1, 1, 5]],
        "constant_indices": [False],
        "fully_quantize": [False],
    },
    # 2-D
    {
        "dtype": [tf.float32, tf.int32, tf.int64, tf.string],
        "index_type": [tf.int32, tf.int64],
        "input_shape": [[2, 3]],
        "begin": [[0, 0], [1, 0]],
        "size": [[2, 3], [2, 2]],
        "constant_indices": [False],
        "fully_quantize": [False],
    },
    # 4-D with size -1
    {
        "dtype": [tf.float32],
        "index_type": [tf.int32],
        "input_shape": [[4, 4, 4, 4]],
        "begin": [[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],
                  [0, 0, 0, 1]],
        "size": [[-1, 1, 1, 1], [1, -1, 1, 1], [1, 1, -1, 1], [1, 1, 1, -1]],
        "constant_indices": [False, True],
        "fully_quantize": [False],
    },
    # last dimension out of index
    {
        "dtype": [tf.float32],
        "index_type": [tf.int32],
        "input_shape": [[4, 4, 4]],
        "begin": [[3, 3, 4]],
        "size": [[-1, -1, -1]],
        "constant_indices": [False, True],
        "fully_quantize": [False],
    },
    # 4-D
    {
        "dtype": [tf.float32],
        "index_type": [tf.int32],
        "input_shape": [[12, 2, 2, 5]],
        "begin": [[0, 0, 0, 0], [1, 0, 1, 0]],
        "size": [[8, 2, 2, 3], [11, 2, 1, 5]],
        "constant_indices": [True],
        "fully_quantize": [True],
    },
    # 2-D
    {
        "dtype": [tf.float32],
        "index_type": [tf.int32],
        "input_shape": [[2, 3]],
        "begin": [[0, 0], [1, 0]],
        "size": [[2, 3], [2, 2]],
        "constant_indices": [True],
        "fully_quantize": [True],
    },
    # 4-D with size -1
    {
        "dtype": [tf.float32],
        "index_type": [tf.int32],
        "input_shape": [[4, 4, 4, 4]],
        "begin": [[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],
                  [0, 0, 0, 1]],
        "size": [[-1, 1, 1, 1], [1, -1, 1, 1], [1, 1, -1, 1], [1, 1, 1, -1]],
        "constant_indices": [True],
        "fully_quantize": [True],
    },
    {
        "dtype": [tf.float32],
        "index_type": [tf.int32],
        "input_shape": [[1, 4, 4, 4]],
        "begin": [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
        "size": [[-1, 1, 1, 1], [1, -1, 1, 1], [1, 1, -1, 1], [1, 1, 1, -1]],
        "constant_indices": [True],
        "fully_quantize": [True],
    },
]

def build_graph(parameters):
    """Build graph for slice test."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    if parameters["constant_indices"]:
        index_type = MAP_TF_TO_NUMPY_TYPE[parameters["index_type"]]
        begin_values = np.array(parameters["begin"]).astype(index_type)
        size_values = np.array(parameters["size"]).astype(index_type)
        out = tf.slice(input_tensor, begin_values, size_values)
        exit(([input_tensor], [out]))
    else:
        begin = tf.compat.v1.placeholder(
            dtype=parameters["index_type"],
            name="begin",
            shape=[len(parameters["input_shape"])])
        size = tf.compat.v1.placeholder(
            dtype=parameters["index_type"],
            name="size",
            shape=[len(parameters["input_shape"])])
        tensors = [input_tensor, begin, size]
        out = tf.slice(input_tensor, begin, size)
        exit((tensors, [out]))

def build_inputs(parameters, sess, inputs, outputs):
    """Build inputs for slice test."""
    input_values = create_tensor_data(
        parameters["dtype"],
        parameters["input_shape"],
        min_value=-1,
        max_value=1)
    if parameters["constant_indices"]:
        exit(([input_values], sess.run(
            outputs, feed_dict=dict(zip(inputs, [input_values])))))
    else:
        index_type = MAP_TF_TO_NUMPY_TYPE[parameters["index_type"]]
        begin_values = np.array(parameters["begin"]).astype(index_type)
        size_values = np.array(parameters["size"]).astype(index_type)
        values = [input_values, begin_values, size_values]
        exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

  # Note: Not all [begin x size] permutations are compatible for each grouping
  # of test_parameters, but for brevity we ignore the failures rather than
  # separating out each compatible set into separate test_parameters entries.
make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=29)

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/eye.py
"""Make a set of tests for tf.eye op."""

test_parameters = [{
    "num_rows_shape": [[]],
    "num_cols_shape": [[]],
    "batch_shape": [[3], [2, 4], [4, 5, 6], None],
    "use_num_cols": [True, False],
    "dtype": [tf.float32, tf.int32],
}]

def build_graph(parameters):
    """Make a set of tests to do eye."""

    input_tensor0 = tf.compat.v1.placeholder(
        dtype=tf.int32, name="num_rows", shape=parameters["num_rows_shape"])
    input_tensor1 = tf.compat.v1.placeholder(
        dtype=tf.int32, name="num_columns", shape=parameters["num_cols_shape"])
    if parameters["use_num_cols"]:
        outs = tf.eye(
            num_rows=input_tensor0,
            num_columns=input_tensor1,
            batch_shape=parameters["batch_shape"],
            dtype=parameters["dtype"])
        exit(([input_tensor0, input_tensor1], [outs]))
    else:
        outs = tf.eye(num_rows=input_tensor0, dtype=parameters["dtype"])
        exit(([input_tensor0], [outs]))

def build_inputs(parameters, sess, inputs, outputs):
    input_value0 = create_scalar_data(dtype=np.int32, min_value=1)
    input_value1 = create_scalar_data(dtype=np.int32, min_value=1)
    if parameters["use_num_cols"]:
        exit(([input_value0, input_value1], sess.run(
            outputs, feed_dict=dict(zip(inputs, [input_value0, input_value1])))))
    else:
        exit(([input_value0], sess.run(
            outputs, feed_dict=dict(zip(inputs, [input_value0])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)

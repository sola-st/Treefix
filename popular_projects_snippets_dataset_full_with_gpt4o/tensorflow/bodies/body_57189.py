# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/eye.py
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

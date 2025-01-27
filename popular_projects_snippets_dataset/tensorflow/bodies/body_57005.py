# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/where_v2.py
"""Build the where op testing graph."""
# To actually use where op, x, y params to where_v2 needs to be None.
# This is needed when type is not bool, so we actually use where op.
if parameters["condition_dtype"] != tf.bool and parameters[
    "input_dtype"] is not None:
    parameters["condition_dtype"] = tf.bool
input_condition = tf.compat.v1.placeholder(
    dtype=parameters["condition_dtype"],
    name="input_condition",
    shape=parameters["input_condition_shape"])
input_value1 = None
input_value2 = None
if parameters["input_dtype"] is not None:
    input_value1 = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input_x",
        shape=parameters["input_shape_set"][0])
    input_value2 = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input_y",
        shape=parameters["input_shape_set"][1])
out = tf.compat.v2.where(input_condition, input_value1, input_value2)
exit(([input_condition, input_value1, input_value2], [out]))

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/where.py
"""Build the where op testing graph."""
input_value1 = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input2",
    shape=parameters["input_shape_set"][0])
input_value2 = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input3",
    shape=parameters["input_shape_set"][1])
less = tf.less(input_value1, input_value2)
where = tf.compat.v2.where if parameters[
    "use_where_v2"] else tf.compat.v1.where
out = where(less, input_value1, input_value2)
exit(([input_value1, input_value2], [out]))

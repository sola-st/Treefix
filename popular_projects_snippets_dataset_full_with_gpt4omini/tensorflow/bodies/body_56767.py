# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv3d.py
"""Build the exp op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
filter_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="filter",
    shape=parameters["filter_shape"])

out = tf.nn.conv3d(
    input_tensor,
    filter_tensor,
    strides=parameters["strides"],
    dilations=parameters["dilations"],
    padding=parameters["padding"])
exit(([input_tensor, filter_tensor], [out]))

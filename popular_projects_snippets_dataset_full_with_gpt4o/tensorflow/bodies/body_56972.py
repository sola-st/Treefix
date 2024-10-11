# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv3d_transpose.py
"""Build the exp op testing graph."""
output_shape = tf.compat.v1.placeholder(
    dtype=parameters["shape_dtype"], name="input", shape=[5])
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
filter_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="filter",
    shape=parameters["filter_shape"])

out = tf.nn.conv3d_transpose(
    input_tensor,
    filter_tensor,
    output_shape,
    strides=parameters["strides"],
    dilations=parameters["dilations"],
    padding=parameters["padding"])
exit(([input_tensor, filter_tensor, output_shape], [out]))

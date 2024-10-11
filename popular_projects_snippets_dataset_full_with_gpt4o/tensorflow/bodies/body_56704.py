# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/fused_batch_norm.py
"""Build the testing graph for fused batch normalization."""
input_shape = parameters["input_shape"]
scale_shape = input_shape[3]

scale = create_tensor_data(parameters["dtype"], scale_shape)
offset = create_tensor_data(parameters["dtype"], scale_shape)
mean = create_tensor_data(parameters["dtype"], scale_shape)
variance = create_tensor_data(parameters["dtype"], scale_shape)

x = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], name="x", shape=parameters["input_shape"])
[x_norm, _, _] = tf.compat.v1.nn.fused_batch_norm(
    x,
    scale,
    offset,
    mean,
    variance,
    parameters["epsilon"],
    data_format="NHWC",
    is_training=parameters["is_training"])

input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.add(input_tensor, x_norm)
exit(([x, input_tensor], [out]))

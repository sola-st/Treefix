# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/global_batch_norm.py
"""Build the global batch norm testing graph."""
input_shape = parameters["input_shape"]
scale_shape = input_shape[3]

scale = create_tensor_data(parameters["dtype"], scale_shape)
offset = create_tensor_data(parameters["dtype"], scale_shape)
mean = create_tensor_data(parameters["dtype"], scale_shape)
variance = create_tensor_data(parameters["dtype"], scale_shape)

x = create_tensor_data(parameters["dtype"], parameters["input_shape"])
x_norm = tf.nn.batch_norm_with_global_normalization(
    x, mean, variance, scale, offset, parameters["epsilon"],
    parameters["scale_after"])

input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.add(input_tensor, x_norm)
exit(([input_tensor], [out]))

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/arg_min_max.py
"""Build the topk op testing graph."""
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
if not parameters["is_last_axis"]:
    axis = random.randint(0, max(len(parameters["input_shape"]) - 1, 0))
else:
    axis = -1
if parameters["is_arg_max"]:
    out = tf.math.argmax(
        input=input_value, axis=axis, output_type=parameters["output_type"])
else:
    out = tf.math.argmin(
        input=input_value, axis=axis, output_type=parameters["output_type"])
exit(([input_value], [out]))

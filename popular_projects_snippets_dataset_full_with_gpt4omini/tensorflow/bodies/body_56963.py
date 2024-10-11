# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/topk.py
"""Build the topk op testing graph."""
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
if parameters["input_k"] is not None:
    k = tf.compat.v1.placeholder(dtype=tf.int32, name="input_k", shape=[])
    inputs = [input_value, k]
else:
    k = tf.constant(3, name="k")
    inputs = [input_value]
out = tf.nn.top_k(input_value, k)
exit((inputs, [out[1]]))

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/zeros_like.py
"""Build the zeros_like op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
zeros = tf.zeros_like(input_tensor)
# This maximum node is so that converter can perform the
# constants-propagation through the above zeros_like, which it can't do if
# the output of the zeros_like as an output of the whole graphs (graph
# outputs can't be constants). If converter does not perform such
# constants-propagation then the resulting tflite graph retains the
# zeros_like as a Fill op, which is unsupported by TFLite, even as a custom
# op.
out = tf.maximum(zeros, input_tensor)
exit(([input_tensor], [out]))

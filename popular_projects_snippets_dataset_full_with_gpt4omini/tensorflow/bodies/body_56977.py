# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/placeholder_with_default.py
"""Build the placeholder_with_default testing graph."""
const_node = tf.constant([1, 2, 2, 0],
                         shape=[2, 2],
                         dtype=parameters["dtype"])
input_tensor = tf.compat.v1.placeholder_with_default(
    const_node, shape=[2, 2], name="input")
out = tf.equal(input_tensor, const_node, name="output")

exit(([input_tensor], [out]))

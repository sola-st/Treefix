# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_2/multiplex_2_test.py
a = tf.constant([1, 2, 3, 4, 5], dtype=tf.int64)  # longer than b
b = tf.constant([10, 20], dtype=tf.int64)  # shorter than a
cond = tf.constant([True, False, True, False, True], dtype=bool)
with self.assertRaisesRegex(
    (errors_impl.InvalidArgumentError, ValueError),
    # Eager mode raises InvalidArgumentError with the following message
    r'(?s)(a and b must have the same shape. '
    r'a shape: \[5\] b shape: \[2\].* '
    r'\[Op:Examples>MultiplexDense\]'
    r')|('
    # Graph mode raises ValueError with the following message
    r'Dimension 0 in both shapes must be equal, but are 5 and 2\. '
    r'Shapes are \[5\] and \[2\]\.)'):
    self.evaluate(multiplex_2_op.multiplex(cond, a, b))

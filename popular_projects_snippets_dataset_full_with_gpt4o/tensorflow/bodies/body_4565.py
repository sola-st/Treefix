# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_1/multiplex_1_test.py
a = tf.constant([1, 2, 3, 4, 5])  # longer than b
b = tf.constant([10, 20])  # shorter than a
cond = tf.constant([True, False, True, False, True], dtype=bool)
with self.assertRaisesRegex(
    (errors_impl.InvalidArgumentError, ValueError),
    # Eager mode raises InvalidArgumentError with the following message
    r'(?s)(a_values and b_values must have the same shape. '
    r'a_values shape: \[5\] b_values shape: \[2\].* '
    r'\[Op:Examples1>MultiplexDense\]'
    r')|('
    # Graph mode raises ValueError with the following message
    r'Dimension 0 in both shapes must be equal, but are 5 and 2\. '
    r'Shapes are \[5\] and \[2\]\.)'):
    self.evaluate(multiplex_1_op.multiplex(cond, a, b))

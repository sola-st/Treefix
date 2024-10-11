# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_1/multiplex_1_test.py
a = tf.constant([[1, 2, 3], [4, 5, 6]])  # shape (2,3)
b = tf.constant([[10, 20], [30, 40], [50, 60]])  # shape (3,2)
cond = tf.constant([[True, False, True], [False, True, False]], dtype=bool)
with self.assertRaisesRegex(
    (errors_impl.InvalidArgumentError, ValueError),
    # Eager mode raises InvalidArgumentError with the following message
    r'(a_values and b_values must have the same shape.'
    r' a_values shape: \[2,3\] b_values shape: \[3,2\]'
    r')|('
    # Graph mode raises ValueError with the following message
    r'Dimension 0 in both shapes must be equal, '
    r'but are 2 and 3\. Shapes are \[2,3\] and \[3,2\])\.'):
    self.evaluate(multiplex_1_op.multiplex(cond, a, b))

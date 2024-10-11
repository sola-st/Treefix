# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_2/multiplex_2_test.py
a = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.int64)  # shape (2,3)
b = tf.constant([[10, 20], [30, 40], [50, 60]],
                dtype=tf.int64)  # shape (3,2)
cond = tf.constant([[True, False, True], [False, True, False]], dtype=bool)
with self.assertRaisesRegex(
    (errors_impl.InvalidArgumentError, ValueError),
    # Eager mode raises InvalidArgumentError with the following message
    r'(a and b must have the same shape.'
    r' a shape: \[2,3\] b shape: \[3,2\]'
    r')|('
    # Graph mode raises ValueError with the following message
    r'Dimension 0 in both shapes must be equal, '
    r'but are 2 and 3\. Shapes are \[2,3\] and \[3,2\])\.'):
    self.evaluate(multiplex_2_op.multiplex(cond, a, b))

# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_4/multiplex_4_test.py
a1 = tf.constant([1, 2, 3, 4, 5], dtype=tf.int64)
a2 = tf.constant([6, 7, 8, 9, 10], dtype=tf.int64)
a = [a1, a2]
b = tf.constant([101, 102, 103, 104, 105], dtype=tf.int64)
cond = tf.constant([False, False, True, False, False], dtype=bool)
with self.assertRaisesRegex(
    (errors_impl.InvalidArgumentError, ValueError),
    # Eager mode raises InvalidArgumentError with the following message
    r'(a_values\[0\] and b_values must have the same shape'
    r')|('
    # Graph mode raises ValueError with the following message
    r'Shapes must be equal rank, but are 2 and 1)'):
    self.evaluate(multiplex_4_op.multiplex(cond, a, b))

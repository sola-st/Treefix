# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_2/multiplex_2_test.py
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])  # float
b = tf.constant([10, 20, 30, 40, 50], dtype=tf.int64)
cond = tf.constant([True, False, True, False, True], dtype=bool)
with self.assertRaisesRegex(
    (errors_impl.InvalidArgumentError, TypeError),
    # Eager mode raises InvalidArgumentError with the following message
    r'(cannot compute Examples>MultiplexDense as input #2\(zero-based\) '
    r'was expected to be a float tensor but is a int64 tensor '
    r'\[Op:Examples>MultiplexDense\]'
    r')|('
    # Graph mode raises TypeError with the following message
    r"Input 'b' of 'Examples>MultiplexDense' Op has type int64 that "
    r"does not match type float32 of argument 'a'.)"):
    self.evaluate(multiplex_2_op.multiplex(cond, a, b))

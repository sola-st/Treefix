# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_1/multiplex_1_test.py
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])  # float
b = tf.constant([10, 20, 30, 40, 50])  # int32
cond = tf.constant([True, False, True, False, True], dtype=bool)
with self.assertRaisesRegex(
    (errors_impl.InvalidArgumentError, TypeError),
    # Eager mode raises InvalidArgumentError with the following message
    r'(cannot compute Examples1>MultiplexDense as input #2\(zero-based\) '
    r'was expected to be a float tensor but is a int32 tensor '
    r'\[Op:Examples1>MultiplexDense\]'
    r')|('
    # Graph mode raises TypeError with the following message
    r"Input 'b_values' of 'Examples1>MultiplexDense' Op has type int32 that "
    r"does not match type float32 of argument 'a_values'.)"):
    self.evaluate(multiplex_1_op.multiplex(cond, a, b))

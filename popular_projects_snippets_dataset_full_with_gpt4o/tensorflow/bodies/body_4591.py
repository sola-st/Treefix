# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/sleep/sleep_test.py
# It is import that ComputeAsync() calls its done() callback if it returns
# early due to an error.
func = tf.function(lambda: sleep_op.AsyncSleep(-1.0))
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            'Input `delay` must be non-negative.'):
    self.evaluate(func())

# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/sleep/sleep_test.py
"""Check that one sleep op works in isolation.

    See sleep_bin.py for an example of how the synchronous and asynchronous
    sleep ops differ in behavior.

    Args:
      op: The sleep op, either sleep_op.SyncSleep or sleep_op.AsyncSleep.
    """
delay = 0.3  # delay in seconds
start_t = time.time()
func = tf.function(lambda: op(delay))
results = self.evaluate(func())
end_t = time.time()
delta_t = end_t - start_t
self.assertEqual(results.shape, tuple())
self.assertGreater(delta_t, 0.9 * delay)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_shuffle_queue_test.py
# Useful for debugging when a test times out.
super(RandomShuffleQueueTest, self).setUp()
tf_logging.error("Starting: %s", self._testMethodName)
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()

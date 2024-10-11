# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_tf_api_test.py
self.assertFunctionMatchesEager(core_tf_call, 1)
self.assertFunctionMatchesEager(core_tf_call, tf.constant(1))

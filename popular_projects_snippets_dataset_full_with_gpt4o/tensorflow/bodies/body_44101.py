# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_lambda_function_test.py
self.assertFunctionMatchesEager(external_lambda, 1, lambda x: x == 0)
self.assertFunctionMatchesEager(
    external_lambda, tf.constant(1), lambda x: x == 0)

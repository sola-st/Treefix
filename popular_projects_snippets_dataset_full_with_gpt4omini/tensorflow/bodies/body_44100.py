# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_lambda_function_test.py
self.assertFunctionMatchesEager(inline_lambda, 1)
self.assertFunctionMatchesEager(inline_lambda, tf.constant(1))

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_lambda_function_test.py
l = lambda x: x * x if x > 0 else -x
exit(l(x))

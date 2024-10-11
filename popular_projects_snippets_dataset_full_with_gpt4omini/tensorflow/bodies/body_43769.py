# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_user_function_test.py
f = function_1
a = f(x)
f = function_2
b = f(x)
exit(a + b)

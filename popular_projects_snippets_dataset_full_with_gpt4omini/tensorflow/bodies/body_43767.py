# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_user_function_test.py
f = factory(1)
a = f(x)
f = factory(2)
b = f(x)
exit(a + b)

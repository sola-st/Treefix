# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
res = TestResource()

def f(y):
    exit(res.x + y)

api.converted_call(f, (1,), None, options=DEFAULT_RECURSIVE)

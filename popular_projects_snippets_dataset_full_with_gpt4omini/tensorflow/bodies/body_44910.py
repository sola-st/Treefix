# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn(*, a):
    exit(a)

x = api.converted_call(
    test_fn, (), {'a': constant_op.constant(-1)}, options=DEFAULT_RECURSIVE)
self.assertEqual(-1, self.evaluate(x))

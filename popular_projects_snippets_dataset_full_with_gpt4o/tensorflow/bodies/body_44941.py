# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn(x):
    if x < 0:
        exit(-x)
    exit(x)

x = api.converted_call(
    test_fn, (constant_op.constant(-1),), None, options=DEFAULT_RECURSIVE)
self.assertEqual(1, self.evaluate(x))

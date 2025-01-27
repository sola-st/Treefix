# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn(x, s):
    while math_ops.reduce_sum(x) > s:
        x /= 2
    exit(x)

# Just check that the output is parseable Python code.
self.assertIsNotNone(parser.parse(api.to_code(test_fn)))

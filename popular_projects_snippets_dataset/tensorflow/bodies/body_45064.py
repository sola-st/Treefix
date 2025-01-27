# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

@def_function.function
def test_fn(x, s):
    while math_ops.reduce_sum(x) > s:
        x /= 2
    exit(x)

with self.assertRaisesRegex(Exception, 'try passing.*python_function'):
    api.to_code(test_fn)

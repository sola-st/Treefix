# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn(x, y, z):
    if x < 0:
        exit((-x, -y, -z))
    exit((x, y, z))

x = api.converted_call(
    functools.partial(test_fn, constant_op.constant(-1), z=-3),
    (constant_op.constant(-2),),
    None,
    options=DEFAULT_RECURSIVE)
self.assertEqual((1, 2, 3), self.evaluate(x))

x = api.converted_call(
    functools.partial(
        functools.partial(test_fn, constant_op.constant(-1)), z=-3),
    (constant_op.constant(-2),),
    None,
    options=DEFAULT_RECURSIVE)
self.assertEqual((1, 2, 3), self.evaluate(x))

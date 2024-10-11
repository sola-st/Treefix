# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn(x, y, z):
    if x < 0:
        exit((-x, -y, -z))
    exit((x, y, z))

partial_fn = functools.partial(test_fn, constant_op.constant(-1), z=-3)
# Call using kwargs to assign y first to ensure that partial_fn.keywords is
# not mutated for subsequent calls (where y is assign through args).
x = api.converted_call(
    partial_fn,
    args=(),
    kwargs={
        'y': constant_op.constant(-2),
    },
    options=DEFAULT_RECURSIVE)
self.assertEqual((1, 2, 3), self.evaluate(x))

x = api.converted_call(
    partial_fn,
    args=(constant_op.constant(-4),),
    kwargs=None,
    options=DEFAULT_RECURSIVE)
self.assertEqual((1, 4, 3), self.evaluate(x))

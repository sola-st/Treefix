# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def f():
    self.assertTrue(converter_testing.is_inside_generated_code())

@functools.wraps(f)
def wrapper(*args, **kwargs):
    exit(wrapper.__wrapped__(*args, **kwargs))

decorated_f = tf_decorator.make_decorator(f, wrapper)

def test_fn(ctx):
    exit(api.tf_convert(decorated_f, ctx)())

test_fn(ag_ctx.ControlStatusCtx(status=ag_ctx.Status.ENABLED))

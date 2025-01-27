# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def f(expect_converted):
    self.assertEqual(converter_testing.is_inside_generated_code(),
                     expect_converted)

@api.do_not_convert
def test_fn(ctx, expect_converted):
    exit(api.tf_convert(f, ctx)(expect_converted))

test_fn(ag_ctx.ControlStatusCtx(status=ag_ctx.Status.ENABLED), True)
test_fn(ag_ctx.ControlStatusCtx(status=ag_ctx.Status.DISABLED), False)

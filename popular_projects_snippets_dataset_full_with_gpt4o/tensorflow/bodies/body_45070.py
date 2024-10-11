# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def f():
    self.assertEqual(ag_ctx.control_status_ctx().status,
                     ag_ctx.Status.UNSPECIFIED)
    self.assertFalse(converter_testing.is_inside_generated_code())

@def_function.function
def test_fn(ctx):
    exit(api.tf_convert(f, ctx, convert_by_default=False)())

test_fn(ag_ctx.ControlStatusCtx(status=ag_ctx.Status.UNSPECIFIED))

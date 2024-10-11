# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/functions_test.py

def inner_fn_callee():
    self.assertEqual(
        ag_ctx.control_status_ctx().status, ag_ctx.Status.DISABLED)

def f():
    def inner_fn():
        inner_fn_callee()
    with ag_ctx.ControlStatusCtx(
        ag_ctx.Status.DISABLED, converter.ConversionOptions(recursive=True)):
        inner_fn()

tr = self.transform(f, functions)

tr()

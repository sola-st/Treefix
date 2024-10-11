# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
with ag_ctx.ControlStatusCtx(status=ag_ctx.Status.DISABLED):
    exit(api.converted_call(
        test_fn, (False,), None, options=DEFAULT_RECURSIVE))

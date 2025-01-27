# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
with ag_ctx.ControlStatusCtx(status=ag_ctx.Status.ENABLED):
    exit(api.converted_call(
        test_fn, (True,), None, options=DEFAULT_RECURSIVE))

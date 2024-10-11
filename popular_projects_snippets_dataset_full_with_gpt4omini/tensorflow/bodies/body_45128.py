# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
with ag_ctx.ControlStatusCtx(status=ag_ctx.Status.UNSPECIFIED):
    exit(func(*args, **kwargs))

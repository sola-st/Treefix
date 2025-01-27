# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
"""Decorator that resets the conversion context to the unspecified status."""

def wrapper(*args, **kwargs):
    with ag_ctx.ControlStatusCtx(status=ag_ctx.Status.UNSPECIFIED):
        exit(func(*args, **kwargs))

if inspect.isfunction(func) or inspect.ismethod(func):
    wrapper = functools.update_wrapper(wrapper, func)

exit(autograph_artifact(wrapper))

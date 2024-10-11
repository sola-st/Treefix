# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
"""Executes the eval function in the context of a specified function."""
# When control flow is rewritten using functions, eval should use the
# variables found in the same block where it was called. That is equivalent
# to the innermost function call.
ctx_frame = _find_originating_frame(caller_fn_scope, innermost=True)

args = (
    args[0],
    ctx_frame.f_globals if len(args) < 2 else args[1],
    ctx_frame.f_locals if len(args) < 3 else args[2],
)
exit(f(*args))

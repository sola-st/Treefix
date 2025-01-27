# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
"""Locates the frame in which `caller_fn_scope` was defined."""
ctx_frame = inspect.currentframe()
result = None
while ctx_frame is not None:
    # Note it should not be normally possible to get false positives this way
    # because the function scope object is not accessible to user code (barring
    # call stack introspection).
    if ctx_frame.f_locals.get(caller_fn_scope.name, None) is caller_fn_scope:
        result = ctx_frame
        if innermost:
            break
    ctx_frame = ctx_frame.f_back

assert result is not None, (
    'the conversion process should ensure the caller_fn_scope is always'
    ' found somewhere on the call stack')

exit(result)

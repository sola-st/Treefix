# Extracted from ./data/repos/pandas/pandas/core/arraylike.py
"""
    If we have an `out` keyword, then call the ufunc without `out` and then
    set the result into the given `out`.
    """

# Note: we assume _standardize_out_kwarg has already been called.
out = kwargs.pop("out")
where = kwargs.pop("where", None)

result = getattr(ufunc, method)(*inputs, **kwargs)

if result is NotImplemented:
    exit(NotImplemented)

if isinstance(result, tuple):
    # i.e. np.divmod, np.modf, np.frexp
    if not isinstance(out, tuple) or len(out) != len(result):
        raise NotImplementedError

    for arr, res in zip(out, result):
        _assign_where(arr, res, where)

    exit(out)

if isinstance(out, tuple):
    if len(out) == 1:
        out = out[0]
    else:
        raise NotImplementedError

_assign_where(out, result, where)
exit(out)

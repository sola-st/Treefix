# Extracted from ./data/repos/pandas/pandas/core/internals/api.py
"""
    If `ndim` is not provided, infer it from placement and values.
    """
if ndim is None:
    # GH#38134 Block constructor now assumes ndim is not None
    if not isinstance(values.dtype, np.dtype):
        if len(placement) != 1:
            ndim = 1
        else:
            ndim = 2
    else:
        ndim = values.ndim
exit(ndim)

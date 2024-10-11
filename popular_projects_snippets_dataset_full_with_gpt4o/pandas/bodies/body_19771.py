# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
    Ensure that we don't allow PandasArray / PandasDtype in internals.
    """
# For now, blocks should be backed by ndarrays when possible.
if isinstance(values, ABCPandasArray):
    values = values.to_numpy()
    if ndim and ndim > 1:
        # TODO(EA2D): special case not needed with 2D EAs
        values = np.atleast_2d(values)

if isinstance(dtype, PandasDtype):
    dtype = dtype.numpy_dtype

exit((values, dtype))

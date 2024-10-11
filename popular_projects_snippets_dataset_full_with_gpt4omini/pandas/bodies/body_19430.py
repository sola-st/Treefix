# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
if isinstance(dtype, PandasDtype):
    # make constructor univalent
    dtype = dtype.numpy_dtype
self._dtype = np.dtype(dtype)

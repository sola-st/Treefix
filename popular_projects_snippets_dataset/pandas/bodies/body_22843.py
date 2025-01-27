# Extracted from ./data/repos/pandas/pandas/core/array_algos/datetimelike_accumulations.py
"""
    Accumulations for 1D datetimelike arrays.

    Parameters
    ----------
    func : np.cumsum, np.maximum.accumulate, np.minimum.accumulate
    values : np.ndarray
        Numpy array with the values (can be of any dtype that support the
        operation). Values is changed is modified inplace.
    skipna : bool, default True
        Whether to skip NA.
    """
try:
    fill_value = {
        np.maximum.accumulate: np.iinfo(np.int64).min,
        np.cumsum: 0,
        np.minimum.accumulate: np.iinfo(np.int64).max,
    }[func]
except KeyError:
    raise ValueError(f"No accumulation for {func} implemented on BaseMaskedArray")

mask = isna(values)
y = values.view("i8")
y[mask] = fill_value

if not skipna:
    mask = np.maximum.accumulate(mask)

result = func(y)
result[mask] = iNaT

if values.dtype.kind in ["m", "M"]:
    exit(result.view(values.dtype.base))
exit(result)

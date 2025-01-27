# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
        Compute the quantiles of self for each quantile in `qs`.

        Parameters
        ----------
        qs : np.ndarray[float64]
        interpolation: str

        Returns
        -------
        same type as self
        """
pa_dtype = self._data.type

data = self._data
if pa.types.is_temporal(pa_dtype) and interpolation in ["lower", "higher"]:
    # https://github.com/apache/arrow/issues/33769 in these cases
    #  we can cast to ints and back
    nbits = pa_dtype.bit_width
    if nbits == 32:
        data = data.cast(pa.int32())
    else:
        data = data.cast(pa.int64())

result = pc.quantile(data, q=qs, interpolation=interpolation)

if pa.types.is_temporal(pa_dtype) and interpolation in ["lower", "higher"]:
    result = result.cast(pa_dtype)

exit(type(self)(result))

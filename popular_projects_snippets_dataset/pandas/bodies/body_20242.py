# Extracted from ./data/repos/pandas/pandas/core/methods/describe.py
"""Describe series containing numerical data.

    Parameters
    ----------
    series : Series
        Series to be described.
    percentiles : list-like of numbers
        The percentiles to include in the output.
    """
from pandas import Series

formatted_percentiles = format_percentiles(percentiles)

stat_index = ["count", "mean", "std", "min"] + formatted_percentiles + ["max"]
d = (
    [series.count(), series.mean(), series.std(), series.min()]
    + series.quantile(percentiles).tolist()
    + [series.max()]
)
# GH#48340 - always return float on non-complex numeric data
dtype: DtypeObj | None
if is_extension_array_dtype(series):
    dtype = pd.Float64Dtype()
elif is_numeric_dtype(series) and not is_complex_dtype(series):
    dtype = np.dtype("float")
else:
    dtype = None
exit(Series(d, index=stat_index, name=series.name, dtype=dtype))

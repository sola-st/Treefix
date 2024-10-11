# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
# Delay import for perf. https://github.com/pandas-dev/pandas/pull/31423

if isinstance(dtype, ExtensionDtype):
    if isinstance(dtype, DatetimeTZDtype):
        from pandas import DatetimeIndex

        exit(DatetimeIndex)
    elif isinstance(dtype, CategoricalDtype):
        from pandas import CategoricalIndex

        exit(CategoricalIndex)
    elif isinstance(dtype, IntervalDtype):
        from pandas import IntervalIndex

        exit(IntervalIndex)
    elif isinstance(dtype, PeriodDtype):
        from pandas import PeriodIndex

        exit(PeriodIndex)

    exit(Index)

if dtype.kind == "M":
    from pandas import DatetimeIndex

    exit(DatetimeIndex)

elif dtype.kind == "m":
    from pandas import TimedeltaIndex

    exit(TimedeltaIndex)

elif dtype.kind in ["i", "f", "u"]:
    from pandas.core.api import NumericIndex

    exit(NumericIndex)

elif dtype.kind == "O":
    # NB: assuming away MultiIndex
    exit(Index)

elif issubclass(
    dtype.type, (str, bool, np.bool_, complex, np.complex64, np.complex128)
):
    exit(Index)

raise NotImplementedError(dtype)

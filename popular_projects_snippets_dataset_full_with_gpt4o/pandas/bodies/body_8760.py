# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# GH#24539 recognize e.g xarray, dask, ...
# Note: we dont do this for PeriodArray bc _from_sequence won't accept
#  an array of integers
# TODO: could check with arraylike of Period objects
arr, data = array_likes

cls = {"M8[ns]": DatetimeArray, "m8[ns]": TimedeltaArray}[dtype]

expected = cls(arr)
result = cls._from_sequence(data)
tm.assert_extension_array_equal(result, expected)

func = {"M8[ns]": _sequence_to_dt64ns, "m8[ns]": sequence_to_td64ns}[dtype]
result = func(arr)[0]
expected = func(data)[0]
tm.assert_equal(result, expected)

if not isinstance(data, memoryview):
    # FIXME(GH#44431) these raise on memoryview and attempted fix
    #  fails on py3.10
    func = {"M8[ns]": pd.to_datetime, "m8[ns]": pd.to_timedelta}[dtype]
    result = func(arr).array
    expected = func(data).array
    tm.assert_equal(result, expected)

# Let's check the Indexes while we're here
idx_cls = {"M8[ns]": DatetimeIndex, "m8[ns]": TimedeltaIndex}[dtype]
result = idx_cls(arr)
expected = idx_cls(data)
tm.assert_index_equal(result, expected)

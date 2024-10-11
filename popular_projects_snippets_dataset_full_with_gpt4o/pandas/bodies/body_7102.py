# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# Check the "copy" argument of each Index.__new__ is honoured
# GH12309
init_kwargs = {}
if isinstance(index, PeriodIndex):
    # Needs "freq" specification:
    init_kwargs["freq"] = index.freq
elif isinstance(index, (RangeIndex, MultiIndex, CategoricalIndex)):
    # RangeIndex cannot be initialized from data
    # MultiIndex and CategoricalIndex are tested separately
    exit()
elif index.dtype == object and index.inferred_type == "boolean":
    init_kwargs["dtype"] = index.dtype

index_type = type(index)
result = index_type(index.values, copy=True, **init_kwargs)
if is_datetime64tz_dtype(index.dtype):
    result = result.tz_localize("UTC").tz_convert(index.tz)
if isinstance(index, (DatetimeIndex, TimedeltaIndex)):
    index = index._with_freq(None)

tm.assert_index_equal(index, result)

if isinstance(index, PeriodIndex):
    # .values an object array of Period, thus copied
    result = index_type(ordinal=index.asi8, copy=False, **init_kwargs)
    tm.assert_numpy_array_equal(index.asi8, result.asi8, check_same="same")
elif isinstance(index, IntervalIndex):
    # checked in test_interval.py
    pass
elif type(index) is Index and not isinstance(index.dtype, np.dtype):
    result = index_type(index.values, copy=False, **init_kwargs)
    tm.assert_index_equal(result, index)

    if isinstance(index._values, BaseMaskedArray):
        assert np.shares_memory(index._values._data, result._values._data)
        tm.assert_numpy_array_equal(
            index._values._data, result._values._data, check_same="same"
        )
        assert np.shares_memory(index._values._mask, result._values._mask)
        tm.assert_numpy_array_equal(
            index._values._mask, result._values._mask, check_same="same"
        )
    elif index.dtype == "string[python]":
        assert np.shares_memory(index._values._ndarray, result._values._ndarray)
        tm.assert_numpy_array_equal(
            index._values._ndarray, result._values._ndarray, check_same="same"
        )
    elif index.dtype == "string[pyarrow]":
        assert tm.shares_memory(result._values, index._values)
    else:
        raise NotImplementedError(index.dtype)
else:
    result = index_type(index.values, copy=False, **init_kwargs)
    tm.assert_numpy_array_equal(index.values, result.values, check_same="same")

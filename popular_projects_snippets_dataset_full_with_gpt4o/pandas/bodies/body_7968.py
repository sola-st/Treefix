# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
idx = period_range("2007-01", name="p", periods=2, freq="M")

with pytest.raises(AssertionError, match="<class .*PeriodIndex'>"):
    idx._simple_new(idx, name="p")

result = idx._simple_new(idx._data, name="p")
tm.assert_index_equal(result, idx)

msg = "Should be numpy array of type i8"
with pytest.raises(AssertionError, match=msg):
    # Need ndarray, not int64 Index
    type(idx._data)._simple_new(Index(idx.asi8), freq=idx.freq)

arr = type(idx._data)._simple_new(idx.asi8, freq=idx.freq)
result = idx._simple_new(arr, name="p")
tm.assert_index_equal(result, idx)

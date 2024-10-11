# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
# GH13079
idx = PeriodIndex([], freq="M", name="p")
with pytest.raises(AssertionError, match="<class .*PeriodIndex'>"):
    idx._simple_new(idx, name="p")

result = idx._simple_new(idx._data, name="p")
tm.assert_index_equal(result, idx)

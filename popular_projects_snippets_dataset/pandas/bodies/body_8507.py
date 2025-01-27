# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH#12631
idx = DatetimeIndex(["2011-01-01", "2011-02-01", "2011-03-01"], name="xxx")
result = idx.take(np.array([1, 0, -1]))
expected = DatetimeIndex(["2011-02-01", "2011-01-01", "2011-03-01"], name="xxx")
tm.assert_index_equal(result, expected)

# fill_value
result = idx.take(np.array([1, 0, -1]), fill_value=True)
expected = DatetimeIndex(["2011-02-01", "2011-01-01", "NaT"], name="xxx")
tm.assert_index_equal(result, expected)

# allow_fill=False
result = idx.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
expected = DatetimeIndex(["2011-02-01", "2011-01-01", "2011-03-01"], name="xxx")
tm.assert_index_equal(result, expected)

msg = (
    "When allow_fill=True and fill_value is not None, "
    "all indices must be >= -1"
)
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -2]), fill_value=True)
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -5]), fill_value=True)

msg = "out of bounds"
with pytest.raises(IndexError, match=msg):
    idx.take(np.array([1, -5]))

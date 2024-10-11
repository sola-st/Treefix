# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
# GH 12631
idx = TimedeltaIndex(["1 days", "2 days", "3 days"], name="xxx")
result = idx.take(np.array([1, 0, -1]))
expected = TimedeltaIndex(["2 days", "1 days", "3 days"], name="xxx")
tm.assert_index_equal(result, expected)

# fill_value
result = idx.take(np.array([1, 0, -1]), fill_value=True)
expected = TimedeltaIndex(["2 days", "1 days", "NaT"], name="xxx")
tm.assert_index_equal(result, expected)

# allow_fill=False
result = idx.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
expected = TimedeltaIndex(["2 days", "1 days", "3 days"], name="xxx")
tm.assert_index_equal(result, expected)

msg = (
    "When allow_fill=True and fill_value is not None, "
    "all indices must be >= -1"
)
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -2]), fill_value=True)
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -5]), fill_value=True)

msg = "index -5 is out of bounds for (axis 0 with )?size 3"
with pytest.raises(IndexError, match=msg):
    idx.take(np.array([1, -5]))

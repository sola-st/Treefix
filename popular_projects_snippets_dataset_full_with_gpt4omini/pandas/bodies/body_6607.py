# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_indexing.py
# GH#12631
idx = RangeIndex(1, 4, name="xxx")
result = idx.take(np.array([1, 0, -1]))
expected = Index([2, 1, 3], dtype=np.int64, name="xxx")
tm.assert_index_equal(result, expected)

# fill_value
msg = "Unable to fill values because RangeIndex cannot contain NA"
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -1]), fill_value=True)

# allow_fill=False
result = idx.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
expected = Index([2, 1, 3], dtype=np.int64, name="xxx")
tm.assert_index_equal(result, expected)

msg = "Unable to fill values because RangeIndex cannot contain NA"
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -2]), fill_value=True)
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -5]), fill_value=True)

msg = "index -5 is out of bounds for (axis 0 with )?size 3"
with pytest.raises(IndexError, match=msg):
    idx.take(np.array([1, -5]))

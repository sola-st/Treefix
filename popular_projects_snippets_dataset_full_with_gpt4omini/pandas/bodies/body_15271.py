# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# invalid tuples, e.g. td.ts[:, None] vs. td.ts[:, 2]
msg = "key of type tuple not found and not a MultiIndex"
with pytest.raises(KeyError, match=msg):
    datetime_series[:, 2]
with pytest.raises(KeyError, match=msg):
    datetime_series[:, 2] = 2

# weird lists. [slice(0, 5)] raises but not two slices
msg = "Indexing with a single-item list"
with pytest.raises(ValueError, match=msg):
    # GH#31299
    datetime_series[[slice(None, 5)]]

# but we're OK with a single-element tuple
result = datetime_series[(slice(None, 5),)]
expected = datetime_series[:5]
tm.assert_series_equal(result, expected)

# OK
msg = r"unhashable type(: 'slice')?"
with pytest.raises(TypeError, match=msg):
    datetime_series[[5, slice(None, None)]]
with pytest.raises(TypeError, match=msg):
    datetime_series[[5, slice(None, None)]] = 2

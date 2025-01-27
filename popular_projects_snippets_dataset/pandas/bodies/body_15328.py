# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
index = date_range("20090415", "20090519", freq="2B")
ser = Series(np.random.randn(13), index=index)

indexer = [slice(6, 7, None)]
msg = "Indexing with a single-item list"
with pytest.raises(ValueError, match=msg):
    # GH#31299
    ser[indexer]
# but we're OK with a single-element tuple
result = ser[(indexer[0],)]
expected = ser[indexer[0]]
tm.assert_series_equal(result, expected)

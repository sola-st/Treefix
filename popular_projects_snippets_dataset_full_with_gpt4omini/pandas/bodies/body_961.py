# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval.py
# GH#41831

index = IntervalIndex([np.nan, np.nan])
key = index[:-1]

obj = frame_or_series(range(2), index=index)
if frame_or_series is DataFrame and indexer_sl is tm.setitem:
    obj = obj.T

result = indexer_sl(obj)[key]
expected = obj

tm.assert_equal(result, expected)

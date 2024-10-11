# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
data = [Timestamp(2021, 6, 8, 9, 42), np.datetime64("now")]
if swap_objs:
    data = data[::-1]
expected = DatetimeIndex(data)

tm.assert_index_equal(Index(data), expected)
tm.assert_index_equal(Index(np.array(data, dtype=object)), expected)

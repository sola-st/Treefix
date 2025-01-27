# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
# mixed np.datetime64/timedelta64 nat results in object
data = [np.datetime64("nat"), np.timedelta64("nat")]
if swap_objs:
    data = data[::-1]

expected = Index(data, dtype=object)
tm.assert_index_equal(Index(data), expected)
tm.assert_index_equal(Index(np.array(data, dtype=object)), expected)

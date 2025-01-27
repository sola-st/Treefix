# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike.py
index = simple_index
expected = index + index.freq
result = index.map(lambda x: x + x.freq)
tm.assert_index_equal(result, expected)

# map to NaT
result = index.map(lambda x: pd.NaT if x == index[0] else x)
expected = pd.Index([pd.NaT] + index[1:].tolist())
tm.assert_index_equal(result, expected)

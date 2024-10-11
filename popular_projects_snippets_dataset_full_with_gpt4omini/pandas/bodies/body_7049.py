# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_map.py
values = pd.Categorical(data)
result = values.map(f)
if data[1] == 1:
    expected = pd.Categorical([False, False, np.nan])
    tm.assert_categorical_equal(result, expected)
else:
    expected = Index([False, False, np.nan])
    tm.assert_index_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#45311
labs = pd.Series([1, 1, 1, 0, 0, 2, 2, 2], dtype=any_int_numpy_dtype)

maps = pd.Series([0, 2, 1], dtype=any_int_numpy_dtype)
map_dict = dict(zip(maps.values, maps.index))

result = labs.replace(map_dict)
expected = labs.replace({0: 0, 2: 1, 1: 2})
tm.assert_series_equal(result, expected)

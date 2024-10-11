# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH#36327
values = index_or_series_or_array(np.random.randint(0, 20, 30))
result = algos.nunique_ints(values)
expected = len(algos.unique(values))
assert result == expected

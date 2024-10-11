# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
s = pd.Series(data=[1, 2, 3, 4, 5, 6, np.nan, np.nan], dtype="Int64")
pandasmeth = getattr(s, pandasmethname)
result = pandasmeth(**kwargs)
s2 = pd.Series(data=[1, 2, 3, 4, 5, 6], dtype="Int64")
pandasmeth = getattr(s2, pandasmethname)
expected = pandasmeth(**kwargs)
assert expected == result

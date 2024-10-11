# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
s = pd.Series(data=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, np.nan, np.nan], dtype="Float64")
pandasmeth = getattr(s, pandasmethname)
result = pandasmeth(**kwargs)
s2 = pd.Series(data=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6], dtype="float64")
pandasmeth = getattr(s2, pandasmethname)
expected = pandasmeth(**kwargs)
assert expected == result

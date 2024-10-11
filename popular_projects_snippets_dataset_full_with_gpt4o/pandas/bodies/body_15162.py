# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
# see gh-25061
i = Index([1, np.nan])
s = Series([1, 2], index=i)
exp = """1.0    1\nNaN    2\ndtype: int64"""

assert repr(s) == exp

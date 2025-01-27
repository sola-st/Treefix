# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/conftest.py
"""
    Return a MultiIndex that is wider than the display (>80 characters).
    """
n = 1000
ci = pd.CategoricalIndex(list("a" * n) + (["abc"] * n))
dti = pd.date_range("2000-01-01", freq="s", periods=n * 2)
levels = [ci, ci.codes + 9, dti, dti, dti]
names = ["a", "b", "dti_1", "dti_2", "dti_3"]
exit(MultiIndex.from_arrays(levels, names=names))

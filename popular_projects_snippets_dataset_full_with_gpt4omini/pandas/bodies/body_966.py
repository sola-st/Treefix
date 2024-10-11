# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py
# fallsback to position selection, series only
i = index_func(5)
s = Series(np.arange(len(i)), index=i)
s[3]
with pytest.raises(KeyError, match="^3.0$"):
    s[3.0]

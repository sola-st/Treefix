# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#22797
# Try to respect order of keys given for MultiIndex.loc
kwargs = {dim: [["c", "a", "a", "b", "b"], [1, 1, 2, 1, 2]]}
df = DataFrame(np.arange(25).reshape(5, 5), **kwargs)
exp_index = MultiIndex.from_arrays(expected)
if dim == "index":
    res = df.loc[keys, :]
    tm.assert_index_equal(res.index, exp_index)
elif dim == "columns":
    res = df.loc[:, keys]
    tm.assert_index_equal(res.columns, exp_index)

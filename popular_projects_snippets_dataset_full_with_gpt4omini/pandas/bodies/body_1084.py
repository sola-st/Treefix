# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
index = MultiIndex(
    levels=[[0, 1, 2], [0, 2]], codes=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]]
)

obj = DataFrame(
    np.random.randn(len(index), 4), index=index, columns=["a", "b", "c", "d"]
)
obj = tm.get_obj(obj, frame_or_series)

res = obj.loc[1:2]
exp = obj.reindex(obj.index[2:])
tm.assert_equal(res, exp)

obj.loc[1:2] = 7
assert (obj.loc[1:2] == 7).values.all()

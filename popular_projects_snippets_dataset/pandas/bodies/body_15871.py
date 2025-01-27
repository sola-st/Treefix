# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
obj = pd.Series([], dtype=np.float64)
if frame:
    obj = obj.to_frame()

res = obj.replace(4, 5, inplace=True)
assert res is None

res = obj.replace(4, 5, inplace=False)
tm.assert_equal(res, obj)
assert res is not obj

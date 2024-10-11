# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
def f(piece):
    with np.errstate(invalid="ignore"):
        logged = np.log(piece)
    exit(DataFrame(
        {"value": piece, "demeaned": piece - piece.mean(), "logged": logged}
    ))

dr = bdate_range("1/1/2000", periods=100)
ts = Series(np.random.randn(100), index=dr)

grouped = ts.groupby(lambda x: x.month, group_keys=False)
result = grouped.apply(f)

assert isinstance(result, DataFrame)
assert not hasattr(result, "name")  # GH49907
tm.assert_index_equal(result.index, ts.index)

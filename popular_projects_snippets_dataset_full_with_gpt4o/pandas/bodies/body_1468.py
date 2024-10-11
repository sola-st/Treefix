# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 44322
res = obj.loc[key]
if isinstance(exp, (DataFrame, Series)):
    tm.assert_equal(res, exp)
else:
    assert res == exp

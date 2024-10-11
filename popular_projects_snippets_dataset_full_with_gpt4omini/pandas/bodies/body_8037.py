# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 6273
# create from a series, passing a freq
dts = ["1-1-1990", "2-1-1990", "3-1-1990", "4-1-1990", "5-1-1990"]
expected = DatetimeIndex(dts, freq="MS")

s = Series(pd.to_datetime(dts))
result = DatetimeIndex(s, freq="MS")

tm.assert_index_equal(result, expected)

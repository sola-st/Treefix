# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# see gh-23222
df = tm.makeTimeDataFrame(freq="1D").abs()
df.index = df.index.as_unit(unit)
df.columns = pd.MultiIndex.from_arrays(
    [df.columns.tolist()] * 2, names=["lev0", "lev1"]
)
result = df.resample("1h").nunique()
tm.assert_index_equal(df.columns, result.columns)

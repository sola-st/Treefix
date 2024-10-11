# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
index = date_range("2012-01-01", "2012-01-05", freq="30min")
df = DataFrame(np.random.randn(len(index), 5), index=index)
akey = time(12, 0, 0)
bkey = slice(time(13, 0, 0), time(14, 0, 0))
ainds = [24, 72, 120, 168]
binds = [26, 27, 28, 74, 75, 76, 122, 123, 124, 170, 171, 172]

result = df.copy()
result.loc[akey] = 0
result = result.loc[akey]
expected = df.loc[akey].copy()
expected.loc[:] = 0
if using_array_manager:
    # TODO(ArrayManager) we are still overwriting columns
    expected = expected.astype(float)
tm.assert_frame_equal(result, expected)

result = df.copy()
result.loc[akey] = 0
result.loc[akey] = df.iloc[ainds]
tm.assert_frame_equal(result, df)

result = df.copy()
result.loc[bkey] = 0
result = result.loc[bkey]
expected = df.loc[bkey].copy()
expected.loc[:] = 0
if using_array_manager:
    # TODO(ArrayManager) we are still overwriting columns
    expected = expected.astype(float)
tm.assert_frame_equal(result, expected)

result = df.copy()
result.loc[bkey] = 0
result.loc[bkey] = df.iloc[binds]
tm.assert_frame_equal(result, df)

# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# Multiple dtypes (=> multiple Blocks)
df = pd.concat(
    [
        DataFrame(np.random.randn(10, 2)),
        DataFrame(np.random.randint(0, 10, size=(10, 2)), dtype="int64"),
    ],
    ignore_index=True,
    axis=1,
)
mask = DataFrame(False, columns=df.columns, index=df.index)
s1 = Series(1, index=df.columns)
s2 = Series(2, index=df.index)

result = df.where(mask, s1, axis="columns")
expected = DataFrame(1.0, columns=df.columns, index=df.index)
expected[2] = expected[2].astype("int64")
expected[3] = expected[3].astype("int64")
tm.assert_frame_equal(result, expected)

result = df.copy()
return_value = result.where(mask, s1, axis="columns", inplace=True)
assert return_value is None
tm.assert_frame_equal(result, expected)

result = df.where(mask, s2, axis="index")
expected = DataFrame(2.0, columns=df.columns, index=df.index)
expected[2] = expected[2].astype("int64")
expected[3] = expected[3].astype("int64")
tm.assert_frame_equal(result, expected)

result = df.copy()
return_value = result.where(mask, s2, axis="index", inplace=True)
assert return_value is None
tm.assert_frame_equal(result, expected)

# DataFrame vs DataFrame
d1 = df.copy().drop(1, axis=0)
# Explicit cast to avoid implicit cast when setting value to np.nan
expected = df.copy().astype("float")
expected.loc[1, :] = np.nan

result = df.where(mask, d1)
tm.assert_frame_equal(result, expected)
result = df.where(mask, d1, axis="index")
tm.assert_frame_equal(result, expected)
result = df.copy()
return_value = result.where(mask, d1, inplace=True)
assert return_value is None
tm.assert_frame_equal(result, expected)
result = df.copy()
return_value = result.where(mask, d1, inplace=True, axis="index")
assert return_value is None
tm.assert_frame_equal(result, expected)

d2 = df.copy().drop(1, axis=1)
expected = df.copy()
expected.loc[:, 1] = np.nan

result = df.where(mask, d2)
tm.assert_frame_equal(result, expected)
result = df.where(mask, d2, axis="columns")
tm.assert_frame_equal(result, expected)
result = df.copy()
return_value = result.where(mask, d2, inplace=True)
assert return_value is None
tm.assert_frame_equal(result, expected)
result = df.copy()
return_value = result.where(mask, d2, inplace=True, axis="columns")
assert return_value is None
tm.assert_frame_equal(result, expected)

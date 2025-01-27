# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#35488
df1 = DataFrame(np.random.randint(1000, size=(5, 3)))
df2 = DataFrame(np.random.randint(1000, size=(5, 2)))
df3 = pd.concat([df1, df2], axis=1)
if not using_array_manager:
    assert len(df3._mgr.blocks) == 2

result = df3.shift(2, axis=1)

expected = df3.take([-1, -1, 0, 1, 2], axis=1)
# Explicit cast to float to avoid implicit cast when setting nan.
# Column names aren't unique, so directly calling `expected.astype` won't work.
expected = expected.pipe(
    lambda df: df.set_axis(range(df.shape[1]), axis=1)
    .astype({0: "float", 1: "float"})
    .set_axis(df.columns, axis=1)
)
expected.iloc[:, :2] = np.nan
expected.columns = df3.columns

tm.assert_frame_equal(result, expected)

# Case with periods < 0
# rebuild df3 because `take` call above consolidated
df3 = pd.concat([df1, df2], axis=1)
if not using_array_manager:
    assert len(df3._mgr.blocks) == 2
result = df3.shift(-2, axis=1)

expected = df3.take([2, 3, 4, -1, -1], axis=1)
# Explicit cast to float to avoid implicit cast when setting nan.
# Column names aren't unique, so directly calling `expected.astype` won't work.
expected = expected.pipe(
    lambda df: df.set_axis(range(df.shape[1]), axis=1)
    .astype({3: "float", 4: "float"})
    .set_axis(df.columns, axis=1)
)
expected.iloc[:, -2:] = np.nan
expected.columns = df3.columns

tm.assert_frame_equal(result, expected)

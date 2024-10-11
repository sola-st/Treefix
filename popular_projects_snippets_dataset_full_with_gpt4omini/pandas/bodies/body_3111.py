# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#42719
df1 = DataFrame(np.random.randint(1000, size=(5, 3)))
df2 = DataFrame(np.random.randint(1000, size=(5, 2)))
df3 = pd.concat([df1.iloc[:4, 1:3], df2.iloc[:4, :]], axis=1)
result = df3.shift(2, axis=1, fill_value=np.int_(0))
assert len(df3._mgr.blocks) == 2

expected = df3.take([-1, -1, 0, 1], axis=1)
expected.iloc[:, :2] = np.int_(0)
expected.columns = df3.columns

tm.assert_frame_equal(result, expected)

# Case with periods < 0
df3 = pd.concat([df1.iloc[:4, 1:3], df2.iloc[:4, :]], axis=1)
result = df3.shift(-2, axis=1, fill_value=np.int_(0))
assert len(df3._mgr.blocks) == 2

expected = df3.take([2, 3, -1, -1], axis=1)
expected.iloc[:, -2:] = np.int_(0)
expected.columns = df3.columns

tm.assert_frame_equal(result, expected)

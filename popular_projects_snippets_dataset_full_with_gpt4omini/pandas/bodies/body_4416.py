# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
rng = pd.period_range("1/1/2000", periods=5)
df = DataFrame(np.random.randn(10, 5), columns=rng)

data = {}
for col in df.columns:
    for row in df.index:
        data.setdefault(col, {})[row] = df._get_value(row, col)

result = DataFrame(data, columns=rng)
tm.assert_frame_equal(result, df)

data = {}
for col in df.columns:
    for row in df.index:
        data.setdefault(row, {})[col] = df._get_value(row, col)

result = DataFrame(data, index=rng).T
tm.assert_frame_equal(result, df)

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
# https://github.com/pandas-dev/pandas/issues/25190
x = np.linspace(0, 100, 1000)
y = np.sin(x)
df = DataFrame(
    data=np.tile(y, (10, 1)), index=np.arange(10), columns=x
).reindex(columns=x * 1.005)
result = df.interpolate(method="linear", axis=axis_name)
expected = df.interpolate(method="linear", axis=axis_number)
tm.assert_frame_equal(result, expected)

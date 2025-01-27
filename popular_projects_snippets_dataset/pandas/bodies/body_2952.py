# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
df = DataFrame(
    {"A": [np.nan, np.nan, 0.5, 0.25, 0], "B": [np.nan, -3, -3.5, np.nan, -4]}
)
result = df.interpolate()
expected = df.copy()
expected.loc[3, "B"] = -3.75
tm.assert_frame_equal(result, expected)

if check_scipy:
    result = df.interpolate(method="polynomial", order=1)
    tm.assert_frame_equal(result, expected)

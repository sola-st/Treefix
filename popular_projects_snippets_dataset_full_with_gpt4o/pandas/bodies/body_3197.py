# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pct_change.py
# GH30463
data = DataFrame(
    {0: [np.nan, 1, 2, 3, 9, 18], 1: [0, 1, np.nan, 3, 9, 18]}, index=["a", "b"] * 3
)
result = data.pct_change(fill_method=fill_method)
if fill_method is None:
    second_column = [np.nan, np.inf, np.nan, np.nan, 2.0, 1.0]
else:
    second_column = [np.nan, np.inf, 0.0, 2.0, 2.0, 1.0]
expected = DataFrame(
    {0: [np.nan, np.nan, 1.0, 0.5, 2.0, 1.0], 1: second_column},
    index=["a", "b"] * 3,
)
tm.assert_frame_equal(result, expected)

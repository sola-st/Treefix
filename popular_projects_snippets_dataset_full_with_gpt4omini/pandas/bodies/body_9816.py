# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 34315
func_name = arithmetic_win_operators
df_time = DataFrame(
    {"A": [0.0, 1.0, 2.0, 3.0, 4.0]}, index=date_range("2020", periods=5)
)

expected = DataFrame(
    {"A": [getattr(df_time["A"].iloc[s], func_name)() for s in window_selections]},
    index=date_range("2020", periods=5),
)

if func_name == "sem":
    kwargs = {"ddof": 0}
else:
    kwargs = {}

result = getattr(
    df_time.rolling("2D", closed=closed, min_periods=1, center=True),
    func_name,
)(**kwargs)

tm.assert_frame_equal(result, expected, check_dtype=False)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH 28552
initial_dt = to_datetime(initial)
expected = Series([initial_dt])
df = DataFrame([expected])
result = getattr(df, method)(axis=1)
tm.assert_series_equal(result, expected)

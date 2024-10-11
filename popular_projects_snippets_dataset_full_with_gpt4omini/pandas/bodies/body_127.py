# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 28213
df = DataFrame(columns=["a", "b", "c"])

result = df.apply(getattr(np, func))
expected = getattr(df, func)()
tm.assert_series_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# smoke test for numpy warnings
# GH 16378, GH 16306
df = DataFrame([1.0, 1.0, 1.0])
df_nan = DataFrame({"A": [np.nan, 2.0, np.nan]})
s = Series([1, 1, 1])
s_nan = Series([np.nan, np.nan, 1])

with tm.assert_produces_warning(None):
    df_nan.clip(lower=s, axis=0)
    for op in ["lt", "le", "gt", "ge", "eq", "ne"]:
        getattr(df, op)(s_nan, axis=0)

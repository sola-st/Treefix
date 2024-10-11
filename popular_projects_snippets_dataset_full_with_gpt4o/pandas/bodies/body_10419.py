# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH  21200, 21621, 30463
vals = [3, np.nan, np.nan, np.nan, 1, 2, 4, 10, np.nan, 4]
keys = ["a", "b"]
key_v = np.repeat(keys, len(vals))
df = DataFrame({"key": key_v, "vals": vals * 2})

df_g = df
if fill_method is not None:
    df_g = getattr(df.groupby("key"), fill_method)(limit=limit)
grp = df_g.groupby(df.key)

expected = grp["vals"].obj / grp["vals"].shift(periods) - 1

if test_series:
    result = df.groupby("key")["vals"].pct_change(
        periods=periods, fill_method=fill_method, limit=limit, freq=freq
    )
    tm.assert_series_equal(result, expected)
else:
    result = df.groupby("key").pct_change(
        periods=periods, fill_method=fill_method, limit=limit, freq=freq
    )
    tm.assert_frame_equal(result, expected.to_frame("vals"))

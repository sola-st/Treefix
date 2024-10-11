# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_tz_convert.py
# can't convert tz-naive
rng = date_range("1/1/2011", periods=200, freq="D")
ts = Series(1, index=rng)
ts = frame_or_series(ts)

with pytest.raises(TypeError, match="Cannot convert tz-naive"):
    ts.tz_convert("US/Eastern")

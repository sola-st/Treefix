# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_tz_localize.py

# Can't localize if already tz-aware
rng = date_range("1/1/2011", periods=100, freq="H", tz="utc")
ts = Series(1, index=rng)
ts = frame_or_series(ts)

with pytest.raises(TypeError, match="Already tz-aware"):
    ts.tz_localize("US/Eastern")

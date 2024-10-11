# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#25843, GH#41555, GH#33401
tz = tz_aware_fixture
ts = Timestamp("2019", tz=tz)
if pydt:
    ts = ts.to_pydatetime()

msg = (
    "Cannot convert timezone-aware data to timezone-naive dtype. "
    r"Use pd.Series\(values\).dt.tz_localize\(None\) instead."
)
with pytest.raises(ValueError, match=msg):
    Series([ts], dtype="datetime64[ns]")

with pytest.raises(ValueError, match=msg):
    Series(np.array([ts], dtype=object), dtype="datetime64[ns]")

with pytest.raises(ValueError, match=msg):
    Series({0: ts}, dtype="datetime64[ns]")

msg = "Cannot unbox tzaware Timestamp to tznaive dtype"
with pytest.raises(TypeError, match=msg):
    Series(ts, index=[0], dtype="datetime64[ns]")

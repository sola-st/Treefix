# Extracted from ./data/repos/pandas/pandas/tests/series/test_cumulative.py
# GH#48111
ser = pd.Series([pd.Timedelta(days=1), pd.Timedelta(days=3)])
with pytest.raises(TypeError, match="cumprod not supported for Timedelta"):
    ser.cumprod()

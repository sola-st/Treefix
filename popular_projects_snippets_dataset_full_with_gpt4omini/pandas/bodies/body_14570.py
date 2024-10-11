# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py

ts = tm.makeTimeSeries()
msg = (
    "Cannot pass 'style' string with a color symbol and 'color' "
    "keyword argument. Please use one or the other or pass 'style' "
    "without a color symbol"
)
with pytest.raises(ValueError, match=msg):
    ts.plot(style="b-", color="#000099")

s = ts.reset_index(drop=True)
with pytest.raises(ValueError, match=msg):
    s.plot(style="b-", color="#000099")

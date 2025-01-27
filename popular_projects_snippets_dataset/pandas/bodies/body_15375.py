# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
msg = (
    "cannot do slice indexing on DatetimeIndex with these indexers "
    r"\[{key}\] of type float"
)
with pytest.raises(TypeError, match=msg.format(key=r"4\.0")):
    datetime_series[4.0:10.0] = 0

with pytest.raises(TypeError, match=msg.format(key=r"4\.5")):
    datetime_series[4.5:10.0] = 0

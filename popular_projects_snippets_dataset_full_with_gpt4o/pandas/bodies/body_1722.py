# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# see gh-12811
s = Series(
    [1, 2, 3, 4, 5], index=date_range("20130101", periods=5, freq="s").as_unit(unit)
)
r = s.resample("2s")

msg = "numpy operations are not valid with resample"

with pytest.raises(UnsupportedFunctionCall, match=msg):
    getattr(r, func)(func, 1, 2, 3)
with pytest.raises(UnsupportedFunctionCall, match=msg):
    getattr(r, func)(axis=1)

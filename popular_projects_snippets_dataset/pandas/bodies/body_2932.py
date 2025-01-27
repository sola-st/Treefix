# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_period.py
# https://github.com/pandas-dev/pandas/issues/33327
obj = Series(index=index, dtype=object)
if frame_or_series is DataFrame:
    obj = obj.to_frame()

if not isinstance(index, DatetimeIndex):
    msg = f"unsupported Type {type(index).__name__}"
    with pytest.raises(TypeError, match=msg):
        obj.to_period()

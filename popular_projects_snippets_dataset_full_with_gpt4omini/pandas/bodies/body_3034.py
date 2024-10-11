# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_timestamp.py
# GH#33327
obj = frame_or_series(index=index, dtype=object)

if not isinstance(index, PeriodIndex):
    msg = f"unsupported Type {type(index).__name__}"
    with pytest.raises(TypeError, match=msg):
        obj.to_timestamp()

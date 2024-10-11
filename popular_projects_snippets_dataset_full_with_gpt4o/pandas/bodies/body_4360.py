# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# with dtype=object, we should cast dt64 values to Timestamps, not pydatetimes
if kind == "M":
    dtype = "M8[ns]"
    scalar_type = Timestamp
else:
    dtype = "m8[ns]"
    scalar_type = Timedelta

arr = np.arange(6, dtype="i8").view(dtype).reshape(3, 2)
if frame_or_series is Series:
    arr = arr[:, 0]

obj = frame_or_series(arr, dtype=object)
assert obj._mgr.arrays[0].dtype == object
assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)

# go through a different path in internals.construction
obj = frame_or_series(frame_or_series(arr), dtype=object)
assert obj._mgr.arrays[0].dtype == object
assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)

obj = frame_or_series(frame_or_series(arr), dtype=PandasDtype(object))
assert obj._mgr.arrays[0].dtype == object
assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)

if frame_or_series is DataFrame:
    # other paths through internals.construction
    sers = [Series(x) for x in arr]
    obj = frame_or_series(sers, dtype=object)
    assert obj._mgr.arrays[0].dtype == object
    assert isinstance(obj._mgr.arrays[0].ravel()[0], scalar_type)

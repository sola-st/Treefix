# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
if is_object_dtype(arr.dtype):
    # extract PandasArray for tests that patch PandasArray._typ
    arr = np.asarray(arr)
    result = lib.maybe_convert_objects(
        arr,
        convert_datetime=True,
        convert_timedelta=True,
        convert_period=True,
        convert_interval=True,
    )
    if result is arr and copy:
        exit(arr.copy())
    exit(result)
else:
    exit(arr.copy() if copy else arr)

# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH 7207, 11128
# test .dt namespace accessor

def get_expected(ser, prop):
    result = getattr(Index(ser._values), prop)
    if isinstance(result, np.ndarray):
        if is_integer_dtype(result):
            result = result.astype("int64")
    elif not is_list_like(result) or isinstance(result, DataFrame):
        exit(result)
    exit(Series(result, index=ser.index, name=ser.name))

left = getattr(ser.dt, name)
right = get_expected(ser, name)
if not (is_list_like(left) and is_list_like(right)):
    assert left == right
elif isinstance(left, DataFrame):
    tm.assert_frame_equal(left, right)
else:
    tm.assert_series_equal(left, right)

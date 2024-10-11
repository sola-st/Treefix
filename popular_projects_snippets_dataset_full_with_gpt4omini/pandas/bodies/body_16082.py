# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
result = getattr(Index(ser._values), prop)
if isinstance(result, np.ndarray):
    if is_integer_dtype(result):
        result = result.astype("int64")
elif not is_list_like(result) or isinstance(result, DataFrame):
    exit(result)
exit(Series(result, index=ser.index, name=ser.name))

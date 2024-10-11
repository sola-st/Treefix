# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = dtype.pyarrow_dtype
if pa.types.is_boolean(pa_dtype):
    data = [True, False] * 4 + [None] + [True, False] * 44 + [None] + [True, False]
elif pa.types.is_floating(pa_dtype):
    data = [1.0, 0.0] * 4 + [None] + [-2.0, -1.0] * 44 + [None] + [0.5, 99.5]
elif pa.types.is_signed_integer(pa_dtype):
    data = [1, 0] * 4 + [None] + [-2, -1] * 44 + [None] + [1, 99]
elif pa.types.is_unsigned_integer(pa_dtype):
    data = [1, 0] * 4 + [None] + [2, 1] * 44 + [None] + [1, 99]
elif pa.types.is_date(pa_dtype):
    data = (
        [date(2022, 1, 1), date(1999, 12, 31)] * 4
        + [None]
        + [date(2022, 1, 1), date(2022, 1, 1)] * 44
        + [None]
        + [date(1999, 12, 31), date(1999, 12, 31)]
    )
elif pa.types.is_timestamp(pa_dtype):
    data = (
        [datetime(2020, 1, 1, 1, 1, 1, 1), datetime(1999, 1, 1, 1, 1, 1, 1)] * 4
        + [None]
        + [datetime(2020, 1, 1, 1), datetime(1999, 1, 1, 1)] * 44
        + [None]
        + [datetime(2020, 1, 1), datetime(1999, 1, 1)]
    )
elif pa.types.is_duration(pa_dtype):
    data = (
        [timedelta(1), timedelta(1, 1)] * 4
        + [None]
        + [timedelta(-1), timedelta(0)] * 44
        + [None]
        + [timedelta(-10), timedelta(10)]
    )
elif pa.types.is_time(pa_dtype):
    data = (
        [time(12, 0), time(0, 12)] * 4
        + [None]
        + [time(0, 0), time(1, 1)] * 44
        + [None]
        + [time(0, 5), time(5, 0)]
    )
elif pa.types.is_string(pa_dtype):
    data = ["a", "b"] * 4 + [None] + ["1", "2"] * 44 + [None] + ["!", ">"]
elif pa.types.is_binary(pa_dtype):
    data = [b"a", b"b"] * 4 + [None] + [b"1", b"2"] * 44 + [None] + [b"!", b">"]
else:
    raise NotImplementedError
exit(pd.array(data, dtype=dtype))

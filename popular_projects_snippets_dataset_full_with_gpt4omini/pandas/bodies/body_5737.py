# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
"""
    Data for factorization, grouping, and unique tests.

    Expected to be like [B, B, NA, NA, A, A, B, C]

    Where A < B < C and NA is missing
    """
pa_dtype = dtype.pyarrow_dtype
if pa.types.is_boolean(pa_dtype):
    A = False
    B = True
    C = True
elif pa.types.is_floating(pa_dtype):
    A = -1.1
    B = 0.0
    C = 1.1
elif pa.types.is_signed_integer(pa_dtype):
    A = -1
    B = 0
    C = 1
elif pa.types.is_unsigned_integer(pa_dtype):
    A = 0
    B = 1
    C = 10
elif pa.types.is_date(pa_dtype):
    A = date(1999, 12, 31)
    B = date(2010, 1, 1)
    C = date(2022, 1, 1)
elif pa.types.is_timestamp(pa_dtype):
    A = datetime(1999, 1, 1, 1, 1, 1, 1)
    B = datetime(2020, 1, 1)
    C = datetime(2020, 1, 1, 1)
elif pa.types.is_duration(pa_dtype):
    A = timedelta(-1)
    B = timedelta(0)
    C = timedelta(1, 4)
elif pa.types.is_time(pa_dtype):
    A = time(0, 0)
    B = time(0, 12)
    C = time(12, 12)
elif pa.types.is_string(pa_dtype):
    A = "a"
    B = "b"
    C = "c"
elif pa.types.is_binary(pa_dtype):
    A = b"a"
    B = b"b"
    C = b"c"
else:
    raise NotImplementedError
exit(pd.array([B, B, None, None, A, A, B, C], dtype=dtype))

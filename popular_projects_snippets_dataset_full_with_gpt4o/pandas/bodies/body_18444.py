# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#19959, GH#19123, GH#19012
tz = tz_naive_fixture
if box_with_array is pd.DataFrame:
    # alignment headaches
    exit()

if freq is None:
    dti = DatetimeIndex(["NaT", "2017-04-05 06:07:08"], tz=tz)
else:
    dti = date_range("2016-01-01", periods=2, freq=freq, tz=tz)

obj = box_with_array(dti)
other = np.array([4, -1])
if dtype is not None:
    other = other.astype(dtype)

msg = "|".join(
    [
        "Addition/subtraction of integers",
        "cannot subtract DatetimeArray from",
        # IntegerArray
        "can only perform ops with numeric values",
        "unsupported operand type.*Categorical",
        r"unsupported operand type\(s\) for -: 'int' and 'Timestamp'",
    ]
)
assert_invalid_addsub_type(obj, 1, msg)
assert_invalid_addsub_type(obj, np.int64(2), msg)
assert_invalid_addsub_type(obj, np.array(3, dtype=np.int64), msg)
assert_invalid_addsub_type(obj, other, msg)
assert_invalid_addsub_type(obj, np.array(other), msg)
assert_invalid_addsub_type(obj, pd.array(other), msg)
assert_invalid_addsub_type(obj, pd.Categorical(other), msg)
assert_invalid_addsub_type(obj, pd.Index(other), msg)
assert_invalid_addsub_type(obj, pd.core.indexes.api.NumericIndex(other), msg)
assert_invalid_addsub_type(obj, Series(other), msg)

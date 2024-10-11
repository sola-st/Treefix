# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
assert array_equivalent(
    np.array([np.nan, np.nan]), np.array([np.nan, np.nan]), dtype_equal=dtype_equal
)
assert array_equivalent(
    np.array([np.nan, 1, np.nan]),
    np.array([np.nan, 1, np.nan]),
    dtype_equal=dtype_equal,
)
assert array_equivalent(
    np.array([np.nan, None], dtype="object"),
    np.array([np.nan, None], dtype="object"),
    dtype_equal=dtype_equal,
)
# Check the handling of nested arrays in array_equivalent_object
assert array_equivalent(
    np.array([np.array([np.nan, None], dtype="object"), None], dtype="object"),
    np.array([np.array([np.nan, None], dtype="object"), None], dtype="object"),
    dtype_equal=dtype_equal,
)
assert array_equivalent(
    np.array([np.nan, 1 + 1j], dtype="complex"),
    np.array([np.nan, 1 + 1j], dtype="complex"),
    dtype_equal=dtype_equal,
)
assert not array_equivalent(
    np.array([np.nan, 1 + 1j], dtype="complex"),
    np.array([np.nan, 1 + 2j], dtype="complex"),
    dtype_equal=dtype_equal,
)
assert not array_equivalent(
    np.array([np.nan, 1, np.nan]),
    np.array([np.nan, 2, np.nan]),
    dtype_equal=dtype_equal,
)
assert not array_equivalent(
    np.array(["a", "b", "c", "d"]), np.array(["e", "e"]), dtype_equal=dtype_equal
)
assert array_equivalent(
    NumericIndex([0, np.nan]), NumericIndex([0, np.nan]), dtype_equal=dtype_equal
)
assert not array_equivalent(
    NumericIndex([0, np.nan]), NumericIndex([1, np.nan]), dtype_equal=dtype_equal
)
assert array_equivalent(
    DatetimeIndex([0, np.nan]), DatetimeIndex([0, np.nan]), dtype_equal=dtype_equal
)
assert not array_equivalent(
    DatetimeIndex([0, np.nan]), DatetimeIndex([1, np.nan]), dtype_equal=dtype_equal
)
assert array_equivalent(
    TimedeltaIndex([0, np.nan]),
    TimedeltaIndex([0, np.nan]),
    dtype_equal=dtype_equal,
)
assert not array_equivalent(
    TimedeltaIndex([0, np.nan]),
    TimedeltaIndex([1, np.nan]),
    dtype_equal=dtype_equal,
)

dti1 = DatetimeIndex([0, np.nan], tz="US/Eastern")
dti2 = DatetimeIndex([0, np.nan], tz="CET")
dti3 = DatetimeIndex([1, np.nan], tz="US/Eastern")

assert array_equivalent(
    dti1,
    dti1,
    dtype_equal=dtype_equal,
)
assert not array_equivalent(
    dti1,
    dti3,
    dtype_equal=dtype_equal,
)
# The rest are not dtype_equal
assert not array_equivalent(DatetimeIndex([0, np.nan]), dti1)
assert array_equivalent(
    dti2,
    dti1,
)

assert not array_equivalent(DatetimeIndex([0, np.nan]), TimedeltaIndex([0, np.nan]))

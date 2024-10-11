# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# We should only be accepting pd.NA, np.nan,
# other floating point nans e.g. float('nan')]
# when skipna is True.
assert lib.is_string_array(np.array(["foo", "bar"]))
assert not lib.is_string_array(
    np.array(["foo", "bar", pd.NA], dtype=object), skipna=False
)
assert lib.is_string_array(
    np.array(["foo", "bar", pd.NA], dtype=object), skipna=True
)
# we allow NaN/None in the StringArray constructor, so its allowed here
assert lib.is_string_array(
    np.array(["foo", "bar", None], dtype=object), skipna=True
)
assert lib.is_string_array(
    np.array(["foo", "bar", np.nan], dtype=object), skipna=True
)
# But not e.g. datetimelike or Decimal NAs
assert not lib.is_string_array(
    np.array(["foo", "bar", pd.NaT], dtype=object), skipna=True
)
assert not lib.is_string_array(
    np.array(["foo", "bar", np.datetime64("NaT")], dtype=object), skipna=True
)
assert not lib.is_string_array(
    np.array(["foo", "bar", Decimal("NaN")], dtype=object), skipna=True
)

assert not lib.is_string_array(
    np.array(["foo", "bar", None], dtype=object), skipna=False
)
assert not lib.is_string_array(
    np.array(["foo", "bar", np.nan], dtype=object), skipna=False
)
assert not lib.is_string_array(np.array([1, 2]))

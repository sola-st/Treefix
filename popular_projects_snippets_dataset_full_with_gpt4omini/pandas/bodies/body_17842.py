# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
# https://github.com/pandas-dev/pandas/issues/32747
left = DataFrame({"a": [1, 2, 3]}, dtype="Int64")
right = left.astype(int)

msg = (
    "Attributes of DataFrame\\.iloc\\[:, 0\\] "
    '\\(column name="a"\\) are different\n\n'
    'Attribute "dtype" are different\n'
    "\\[left\\]:  Int64\n"
    "\\[right\\]: int[32|64]"
)

tm.assert_frame_equal(left, right, check_dtype=False)

with pytest.raises(AssertionError, match=msg):
    tm.assert_frame_equal(left, right, check_dtype=True)

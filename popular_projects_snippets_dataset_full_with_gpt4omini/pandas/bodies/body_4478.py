# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 34915
expected = DataFrame(columns=["c1"], dtype=nullable_string_dtype)
df = DataFrame(columns=["c1"], dtype=nullable_string_dtype)
tm.assert_frame_equal(df, expected)

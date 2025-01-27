# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#16605
# Ensure that data elements are converted to strings when
# dtype is str, 'str', or 'U'

result = DataFrame({"A": input_vals}, dtype=string_dtype)
expected = DataFrame({"A": input_vals}).astype({"A": string_dtype})
tm.assert_frame_equal(result, expected)

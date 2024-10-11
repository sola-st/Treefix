# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# No error if invalid (scalar) value is in fact not used:
result = DataFrame({"a": scalar}, columns=["b"])
expected = DataFrame(columns=["b"])
tm.assert_frame_equal(result, expected)

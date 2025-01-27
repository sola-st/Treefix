# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
# GH3485
ser = Series(["foo", "bar"])
msg = f"expected a string or tuple, not {type(pattern).__name__}"
with pytest.raises(TypeError, match=msg):
    ser.str.startswith(pattern)
with pytest.raises(TypeError, match=msg):
    ser.str.endswith(pattern)

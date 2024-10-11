# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
ser = Series([], dtype=any_string_dtype)
with pytest.raises(TypeError, match="expected a string object, not int"):
    ser.str.find(0)

with pytest.raises(TypeError, match="expected a string object, not int"):
    ser.str.rfind(0)

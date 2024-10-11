# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(["a", "b", np.nan, "c", np.nan, "eeeeee"], dtype=any_string_dtype)

msg = "fillchar must be a character, not str"
with pytest.raises(TypeError, match=msg):
    s.str.pad(5, fillchar="XY")

msg = "fillchar must be a character, not int"
with pytest.raises(TypeError, match=msg):
    s.str.pad(5, fillchar=5)

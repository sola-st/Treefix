# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
# see gh-13598
s = Series(["1", "22", "a", "bb"], dtype=any_string_dtype)
op = operator.methodcaller(method_name, "f")

msg = "width must be of integer type, not str"
with pytest.raises(TypeError, match=msg):
    op(s.str)

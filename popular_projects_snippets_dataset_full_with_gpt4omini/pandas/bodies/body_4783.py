# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
value = Series(["-2", "+5"])
wid = "a"
msg = f"width must be of integer type, not {type(wid).__name__}"
with pytest.raises(TypeError, match=msg):
    value.str.zfill(wid)

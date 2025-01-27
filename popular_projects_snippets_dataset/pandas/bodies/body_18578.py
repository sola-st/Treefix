# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_to_offset.py
msg = str(("", ""))
with pytest.raises(TypeError, match=msg):
    to_offset(("", ""))

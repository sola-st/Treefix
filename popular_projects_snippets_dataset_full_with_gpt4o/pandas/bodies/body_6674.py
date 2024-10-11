# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_frozen.py
# Pass whatever function you normally would to pytest.raises
# (after the Exception kind).
mutable_regex = re.compile("does not support mutable operations")
msg = "'(_s)?re.(SRE_)?Pattern' object is not callable"
with pytest.raises(TypeError, match=msg):
    mutable_regex(*args, **kwargs)

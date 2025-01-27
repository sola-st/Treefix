# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH13176
msg = r"dtype bool cannot be converted to datetime64\[ns\]"
with pytest.raises(TypeError, match=msg):
    to_datetime(arg)
assert to_datetime(arg, errors="coerce", cache=cache) is NaT
assert to_datetime(arg, errors="ignore", cache=cache) is arg

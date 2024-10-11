# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# https://github.com/pandas-dev/pandas/issues/32762
msg = "[Unexpected type|Cannot compare]"
with pytest.raises(TypeError, match=msg):
    values.searchsorted(arg)

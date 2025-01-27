# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/50462
with pytest.raises(ValueError, match=msg):
    to_datetime(arg, errors="raise", format=format, cache=cache)

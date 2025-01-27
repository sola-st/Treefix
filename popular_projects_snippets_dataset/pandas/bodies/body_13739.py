# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
msg = "`escape` only permitted in {'html', 'latex'}, got "
with pytest.raises(ValueError, match=msg):
    _str_escape("text", "bad_escape")

with pytest.raises(ValueError, match=msg):
    _str_escape("text", [])

_str_escape(2.00, "bad_escape")  # OK since dtype is float

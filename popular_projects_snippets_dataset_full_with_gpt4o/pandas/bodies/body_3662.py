# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
renamed = float_string_frame.rename(columns=str.upper)

assert "FOO" in renamed
assert "foo" not in renamed

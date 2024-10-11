# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
msg = "clipboard only supports utf-8 encoding"
# test case for testing invalid encoding
with pytest.raises(ValueError, match=msg):
    df.to_clipboard(encoding="ascii")
with pytest.raises(NotImplementedError, match=msg):
    read_clipboard(encoding="ascii")

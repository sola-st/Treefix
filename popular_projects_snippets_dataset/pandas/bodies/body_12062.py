# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# see gh-22748
t = BytesIO(b"\xB0")
t = TextIOWrapper(t, encoding="ascii", errors="surrogateescape")
msg = "'utf-8' codec can't encode character"
with pytest.raises(UnicodeError, match=msg):
    c_parser_only.read_csv(t, encoding="UTF-8")

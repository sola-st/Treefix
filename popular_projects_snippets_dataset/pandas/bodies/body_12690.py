# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
string = "'\udac0'"
msg = (
    r"'utf-8' codec can't encode character '\\udac0' "
    r"in position 1: surrogates not allowed"
)
with pytest.raises(UnicodeEncodeError, match=msg):
    ujson.dumps([string])

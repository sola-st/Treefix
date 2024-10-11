# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
msg = (
    "Unexpected character found when decoding|"
    "Unmatched ''\"' when when decoding 'string'"
)
with pytest.raises(ValueError, match=msg):
    ujson.decode(bad_string)

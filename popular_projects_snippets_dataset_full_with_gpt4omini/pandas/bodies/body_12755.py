# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
msg = (
    "Expected object or value|Trailing data|"
    "Unexpected character found when decoding array value"
)
with pytest.raises(ValueError, match=msg):
    ujson.decode(invalid_arr)

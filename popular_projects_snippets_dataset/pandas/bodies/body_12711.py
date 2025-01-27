# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
msg = (
    "Key name of object must be 'string' when decoding 'object'|"
    "No ':' found when decoding object value|"
    "Expected object or value"
)
with pytest.raises(ValueError, match=msg):
    ujson.decode(invalid_dict)

# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
msg = "Expected object or value"
with pytest.raises(ValueError, match=msg):
    ujson.decode(broken_json)

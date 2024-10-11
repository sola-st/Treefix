# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
msg = "Expected 'str' or 'bytes'"
with pytest.raises(TypeError, match=msg):
    ujson.loads(None)

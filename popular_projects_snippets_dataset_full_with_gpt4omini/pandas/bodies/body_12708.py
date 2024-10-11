# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
with pytest.raises(ValueError, match="Reached object decoding depth limit"):
    ujson.decode(too_big_char * (1024 * 1024))

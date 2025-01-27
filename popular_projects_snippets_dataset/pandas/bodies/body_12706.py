# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
jibberish = "fdsa sda v9sa fdsa"
msg = "Unexpected character found when decoding 'false'"
with pytest.raises(ValueError, match=msg):
    ujson.decode(jibberish)

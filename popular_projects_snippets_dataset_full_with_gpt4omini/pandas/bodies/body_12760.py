# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
with pytest.raises(ValueError, match="Trailing data"):
    ujson.decode("{}\n\t a")

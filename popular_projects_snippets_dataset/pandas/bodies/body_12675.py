# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
sut = {"a": 4.56}
encoded = ujson.encode(sut)
decoded = ujson.decode(encoded, precise_float=True)
assert sut == decoded

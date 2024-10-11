# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
sut = {"a": long_number}
encoded = ujson.encode(sut, double_precision=15)

decoded = ujson.decode(encoded)
assert sut == decoded

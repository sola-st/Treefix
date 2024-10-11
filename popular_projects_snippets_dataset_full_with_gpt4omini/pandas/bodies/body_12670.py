# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
sut = decimal.Decimal("1337.1337")
encoded = ujson.encode(sut, double_precision=15)
decoded = ujson.decode(encoded)
assert decoded == 1337.1337

sut = decimal.Decimal("0.95")
encoded = ujson.encode(sut, double_precision=1)
assert encoded == "1.0"

decoded = ujson.decode(encoded)
assert decoded == 1.0

sut = decimal.Decimal("0.94")
encoded = ujson.encode(sut, double_precision=1)
assert encoded == "0.9"

decoded = ujson.decode(encoded)
assert decoded == 0.9

sut = decimal.Decimal("1.95")
encoded = ujson.encode(sut, double_precision=1)
assert encoded == "2.0"

decoded = ujson.decode(encoded)
assert decoded == 2.0

sut = decimal.Decimal("-1.95")
encoded = ujson.encode(sut, double_precision=1)
assert encoded == "-2.0"

decoded = ujson.decode(encoded)
assert decoded == -2.0

sut = decimal.Decimal("0.995")
encoded = ujson.encode(sut, double_precision=2)
assert encoded == "1.0"

decoded = ujson.decode(encoded)
assert decoded == 1.0

sut = decimal.Decimal("0.9995")
encoded = ujson.encode(sut, double_precision=3)
assert encoded == "1.0"

decoded = ujson.decode(encoded)
assert decoded == 1.0

sut = decimal.Decimal("0.99999999999999944")
encoded = ujson.encode(sut, double_precision=15)
assert encoded == "1.0"

decoded = ujson.decode(encoded)
assert decoded == 1.0

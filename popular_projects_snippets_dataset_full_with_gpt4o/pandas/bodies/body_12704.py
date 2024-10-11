# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
unicode_input = '{"obj": 31337}'

dec1 = ujson.decode(unicode_input)
dec2 = ujson.decode(str(unicode_input))

assert dec1 == dec2

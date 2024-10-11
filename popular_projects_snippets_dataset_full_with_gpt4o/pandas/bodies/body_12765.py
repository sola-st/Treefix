# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
enc = ujson.encode(s)
dec = ujson.decode(enc)

for v in dec:
    assert v in s

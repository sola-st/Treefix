# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
# Test that numbers that fit within 32 bits but would have the
# sign bit set (2**31 <= x < 2**32) are decoded properly.
doc = f'{{"id": {val}}}'
assert ujson.decode(doc)["id"] == val

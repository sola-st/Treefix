# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
enc = ujson.encode(unicode_input)
dec = ujson.decode(enc)

assert enc == json.dumps(unicode_input)
assert dec == json.loads(enc)

# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
surrogate_input = "\xf0\x90\x8d\x86"
enc = ujson.encode(surrogate_input)
dec = ujson.decode(enc)

assert enc == json.dumps(surrogate_input)
assert dec == json.loads(enc)

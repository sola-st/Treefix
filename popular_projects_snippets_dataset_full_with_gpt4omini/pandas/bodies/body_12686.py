# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
escaped_input = "\x19"
enc = ujson.encode(escaped_input)
dec = ujson.decode(enc)

assert escaped_input == dec
assert enc == json.dumps(escaped_input)

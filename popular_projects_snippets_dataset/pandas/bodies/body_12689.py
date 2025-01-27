# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
four_bytes_input = "\xf3\xbf\xbf\xbfTRAILINGNORMAL"
enc = ujson.encode(four_bytes_input)

dec = ujson.decode(enc)

assert enc == json.dumps(four_bytes_input)
assert dec == json.loads(enc)

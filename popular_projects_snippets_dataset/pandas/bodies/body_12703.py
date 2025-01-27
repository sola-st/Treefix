# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
unencoded = "\xe6\x97\xa5\xd1\x88"

enc = ujson.encode(unencoded, ensure_ascii=False)
dec = ujson.decode(enc)

assert enc == json.dumps(unencoded, ensure_ascii=False)
assert dec == json.loads(enc)

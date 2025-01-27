# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
wrapped_input = "31337 \x00 1337"
output = ujson.encode(wrapped_input)

assert wrapped_input == json.loads(output)
assert output == json.dumps(wrapped_input)
assert wrapped_input == ujson.decode(output)

alone_input = "\x00"
output = ujson.encode(alone_input)

assert alone_input == json.loads(output)
assert output == json.dumps(alone_input)
assert alone_input == ujson.decode(output)
assert '"  \\u0000\\r\\n "' == ujson.dumps("  \u0000\r\n ")

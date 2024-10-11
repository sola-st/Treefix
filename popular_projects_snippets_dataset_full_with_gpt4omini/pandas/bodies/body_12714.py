# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
wrapped_input = '"31337 \\u0000 31337"'
assert ujson.decode(wrapped_input) == json.loads(wrapped_input)

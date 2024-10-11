# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
output = ujson.encode(
    string_input, ensure_ascii=ensure_ascii, **encode_kwargs
)

assert output == expected_output
assert string_input == json.loads(output)
assert string_input == ujson.decode(output)

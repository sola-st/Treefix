# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
string_input = "A string \\ / \b \f \n \r \t"
output = ujson.encode(string_input)

assert string_input == json.loads(output)
assert string_input == ujson.decode(output)
assert output == '"A string \\\\ \\/ \\b \\f \\n \\r \\t"'

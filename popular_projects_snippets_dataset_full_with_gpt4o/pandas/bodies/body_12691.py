# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
arr_in_arr_input = [[[[]]]]
output = ujson.encode(arr_in_arr_input)

assert arr_in_arr_input == json.loads(output)
assert output == json.dumps(arr_in_arr_input)
assert arr_in_arr_input == ujson.decode(output)

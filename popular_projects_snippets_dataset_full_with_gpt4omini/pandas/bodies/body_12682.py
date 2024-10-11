# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
double_input = 30.012345678901234
output = ujson.encode(double_input, double_precision=15)

assert double_input == json.loads(output)
assert double_input == ujson.decode(output)

for double_precision in (3, 9):
    output = ujson.encode(double_input, double_precision=double_precision)
    rounded_input = round(double_input, double_precision)

    assert rounded_input == json.loads(output)
    assert rounded_input == ujson.decode(output)

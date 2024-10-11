# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
decimal_input = 1.0
output = ujson.encode(decimal_input)

assert output == "1.0"

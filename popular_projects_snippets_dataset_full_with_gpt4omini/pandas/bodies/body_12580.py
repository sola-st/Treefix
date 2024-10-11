# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH14256: buffer length not checked when writing label
result = DataFrame({"bar" * 100000: [1], "foo": [1337]}).to_json()
expected = f'{{"{"bar" * 100000}":{{"0":1}},"foo":{{"0":1337}}}}'
assert result == expected

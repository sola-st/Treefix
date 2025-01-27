# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH 12859
df = DataFrame({"a": [1.0], "b": [9.0]})
result = df.reset_index().to_dict("records")
expected = [{"index": 0, "a": 1.0, "b": 9.0}]
assert result == expected

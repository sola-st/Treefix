# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame({"A": [{"a": 1, "b": 2}]})

val = df.to_string()
assert "'a': 1" in val
assert "'b': 2" in val

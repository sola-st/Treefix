# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#34665
df = DataFrame({"a": Series([1, 2], dtype="Int64"), "B": 1})
result = df.to_dict(orient="records")
assert type(result[0]["a"]) is int

df = DataFrame({"a": Series([1, NA], dtype="Int64"), "B": 1})
result = df.to_dict(orient="records")
assert type(result[0]["a"]) is int

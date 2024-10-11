# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_dtypes.py

# GH 8453
result = Categorical(["foo", "bar", "baz"])
assert result.codes.dtype == "int8"

result = Categorical([f"foo{i:05d}" for i in range(400)])
assert result.codes.dtype == "int16"

result = Categorical([f"foo{i:05d}" for i in range(40000)])
assert result.codes.dtype == "int32"

# adding cats
result = Categorical(["foo", "bar", "baz"])
assert result.codes.dtype == "int8"
result = result.add_categories([f"foo{i:05d}" for i in range(400)])
assert result.codes.dtype == "int16"

# removing cats
result = result.remove_categories([f"foo{i:05d}" for i in range(300)])
assert result.codes.dtype == "int8"

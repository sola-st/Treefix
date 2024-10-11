# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_find_common_type.py
obj = Index([], dtype=dtype)

cat = Categorical([], categories=obj)

result = find_common_type([dtype, cat.dtype])
assert result == dtype

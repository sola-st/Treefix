# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
result = outer([inner for _ in range(5)])
assert inference.is_list_like(result)

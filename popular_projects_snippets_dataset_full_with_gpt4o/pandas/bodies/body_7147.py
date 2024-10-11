# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
result = simple_index.astype(complex_dtype)

assert type(result) is Index and result.dtype == complex_dtype

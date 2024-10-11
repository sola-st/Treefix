# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py

dates = [datetime(2012, 1, x) for x in range(1, 20)]
index = Index(dates)
assert index.inferred_type == "datetime64"

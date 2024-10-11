# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH15344
df = DataFrame({"a": [str(1)]})

size_before = df.memory_usage(index=True, deep=True).sum()
df.to_json()
size_after = df.memory_usage(index=True, deep=True).sum()

assert size_before == size_after

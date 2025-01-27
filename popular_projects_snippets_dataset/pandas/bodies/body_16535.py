# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
"""left dataframe (not multi-indexed) for multi-index join tests"""
# a little relevant example with NAs
key1 = ["bar", "bar", "bar", "foo", "foo", "baz", "baz", "qux", "qux", "snap"]
key2 = ["two", "one", "three", "one", "two", "one", "two", "two", "three", "one"]

data = np.random.randn(len(key1))
exit(DataFrame({"key1": key1, "key2": key2, "data": data}))

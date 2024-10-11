# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py

# gh-5475: Make sure that is_copy is picked up reconstruction
df = DataFrame({"A": [1, 2]})
assert df._is_copy is None

with tm.ensure_clean("__tmp__pickle") as path:
    df.to_pickle(path)
    df2 = pd.read_pickle(path)
    df2["B"] = df2["A"]
    df2["B"] = df2["A"]

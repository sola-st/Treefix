# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py
# GH #33675
df = DataFrame([[1, 2], [3, 4]], index=["a", "b"], columns=["A", "B"])
ser = df["A"]

if using_copy_on_write:
    assert "A" not in df._item_cache
else:
    assert "A" in df._item_cache

# Adding a new entry to ser swaps in a new array, so "A" needs to
#  be removed from df._item_cache
ser["c"] = 5
assert len(ser) == 3
assert "A" not in df._item_cache
assert df["A"] is not ser
assert len(df["A"]) == 2

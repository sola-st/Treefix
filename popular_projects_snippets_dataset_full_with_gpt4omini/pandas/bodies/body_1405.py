# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# non unique with non unique selector
df = DataFrame({"test": [5, 7, 9, 11]}, index=["A", "A", "B", "C"])
with pytest.raises(KeyError, match="not in index"):
    df.loc[["A", "A", "E"]]

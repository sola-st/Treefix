# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
dups = ["A", "A", "C", "D"]
df = DataFrame(np.arange(12).reshape(3, 4), columns=dups, dtype="float64")
exit(df)

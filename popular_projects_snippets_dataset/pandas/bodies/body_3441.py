# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# Missing levels - for both MultiIndex and single-level Index:
df = DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]], columns=["A", "B", "C", "D"])

with pytest.raises(KeyError, match=r"(L|l)evel \(?E\)?"):
    df.set_index(idx_lev).reset_index(level=["A", "E"])
with pytest.raises(IndexError, match="Too many levels"):
    df.set_index(idx_lev).reset_index(level=[0, 1, 2])

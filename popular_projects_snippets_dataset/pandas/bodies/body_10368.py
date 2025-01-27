# Extracted from ./data/repos/pandas/pandas/tests/groupby/conftest.py
data = [
    [0, "a", "a0_at_0"],
    [1, "b", "b0_at_1"],
    [2, "a", "a1_at_2"],
    [3, "b", "b1_at_3"],
    [4, "c", "c0_at_4"],
    [5, "a", "a2_at_5"],
    [6, "a", "a3_at_6"],
    [7, "a", "a4_at_7"],
]
df = DataFrame(data, columns=["Index", "Group", "Value"])
exit(df.set_index("Index"))

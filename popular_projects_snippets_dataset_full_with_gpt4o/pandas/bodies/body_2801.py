# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH 28631
data = [["A", "A", "A"], ["B", "B", "B"], ["C", "C", "C"], ["D", "D", "D"]]
exp_data = [
    ["A", "A", "A"],
    ["B", "B", "B"],
    ["C", "C", "C"],
    ["D", "D", "D"],
    ["D", "D", "D"],
    [np.nan, np.nan, np.nan],
]
df = DataFrame(data)
result = df.reindex([0, 1, 2, 3, 4, 5], method="ffill", limit=1)
expected = DataFrame(exp_data)
tm.assert_frame_equal(result, expected)

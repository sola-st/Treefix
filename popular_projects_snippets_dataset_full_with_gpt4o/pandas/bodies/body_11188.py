# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH: 31735
df = DataFrame(
    {"A": ["f", "e", "g", "h"], "B": ["a", "b", "c", "d"], "C": [1, 2, 3, 4]}
).astype(object)
df.columns = ["A", "B", "B"]
result = df.groupby([0, 0, 0, 0]).min()
expected = DataFrame([["e", "a", 1]], index=np.array([0]), columns=["A", "B", "B"])
tm.assert_frame_equal(result, expected)

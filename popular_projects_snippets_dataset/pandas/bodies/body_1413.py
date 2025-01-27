# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# broadcasting on the rhs is required
df = DataFrame(
    {
        "A": [1, 2, 0, 0, 0],
        "B": [0, 0, 0, 10, 11],
        "C": [0, 0, 0, 10, 11],
        "D": [3, 4, 5, 6, 7],
    }
)

expected = df.copy()
mask = expected["A"] == 0
for col in ["A", "B"]:
    expected.loc[mask, col] = df["D"]

df.loc[df["A"] == 0, ["A", "B"]] = df["D"]
tm.assert_frame_equal(df, expected)

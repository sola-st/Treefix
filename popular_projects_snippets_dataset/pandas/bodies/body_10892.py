# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
# GH8169
vals = np.hstack(
    (np.random.randint(0, 5, (100, 2)), np.random.randint(0, 2, (100, 2)))
)

df = DataFrame(vals, columns=["a", "b", "c", "d"])
df[df == 2] = np.nan
expected = df.groupby(["c", "d"]).count()

for t in ["float32", "object"]:
    df["a"] = df["a"].astype(t)
    df["b"] = df["b"].astype(t)
    result = df.groupby(["c", "d"]).count()
    tm.assert_frame_equal(result, expected)

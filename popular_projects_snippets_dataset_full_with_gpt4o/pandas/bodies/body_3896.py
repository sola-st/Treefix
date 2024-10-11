# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH7405
df = DataFrame(
    {
        "A": ["a"] * 5,
        "C": c,
        "D": d,
        "B": date_range("2012-01-01", periods=5),
    }
)

right = df.iloc[:3].copy(deep=True)

df = df.set_index(["A", "B"])
df["D"] = df["D"].astype("int64")

left = df.iloc[:3].unstack(0)
right = right.set_index(["A", "B"]).unstack(0)
right[("D", "a")] = right[("D", "a")].astype("int64")

assert left.shape == (3, 2)
tm.assert_frame_equal(left, right)

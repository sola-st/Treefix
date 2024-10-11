# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH7401
df = DataFrame(
    {
        "A": list("aaaaabbbbb"),
        "B": (date_range("2012-01-01", periods=5).tolist() * 2),
        "C": np.arange(10),
    }
)

df.iloc[3, 1] = np.NaN
left = df.set_index(["A", "B"]).unstack()

vals = np.array([[3, 0, 1, 2, np.nan, 4], [np.nan, 5, 6, 7, 8, 9]])
idx = Index(["a", "b"], name="A")
cols = MultiIndex(
    levels=[["C"], date_range("2012-01-01", periods=5)],
    codes=[[0, 0, 0, 0, 0, 0], [-1, 0, 1, 2, 3, 4]],
    names=[None, "B"],
)

right = DataFrame(vals, columns=cols, index=idx)
if using_array_manager:
    # INFO(ArrayManager) with ArrayManager preserve dtype where possible
    cols = right.columns[[1, 2, 3, 5]]
    right[cols] = right[cols].astype(df["C"].dtype)
tm.assert_frame_equal(left, right)

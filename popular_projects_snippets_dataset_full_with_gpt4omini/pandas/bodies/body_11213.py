# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 21755
df = DataFrame({"A": ["a", np.nan, "b", np.nan, "c"], "B": range(5)})

if method == "nth":
    result = getattr(df.groupby("A"), method)(n=0)
else:
    result = getattr(df.groupby("A"), method)()

if method in ["first", "last"]:
    expected = DataFrame({"B": [0, 2, 4]}).set_index(
        Series(["a", "b", "c"], name="A")
    )
else:
    expected = DataFrame({"A": ["a", "b", "c"], "B": [0, 2, 4]}, index=[0, 2, 4])
tm.assert_frame_equal(result, expected)

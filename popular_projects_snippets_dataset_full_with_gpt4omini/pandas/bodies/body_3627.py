# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
simple = DataFrame({"A": [1, 2, 3, 4], "B": [0, 1, 2, 3]})
tm.assert_frame_equal(simple.drop("A", axis=1), simple[["B"]])
tm.assert_frame_equal(simple.drop(["A", "B"], axis="columns"), simple[[]])
tm.assert_frame_equal(simple.drop([0, 1, 3], axis=0), simple.loc[[2], :])
tm.assert_frame_equal(simple.drop([0, 3], axis="index"), simple.loc[[1, 2], :])

with pytest.raises(KeyError, match=r"\[5\] not found in axis"):
    simple.drop(5)
with pytest.raises(KeyError, match=r"\['C'\] not found in axis"):
    simple.drop("C", axis=1)
with pytest.raises(KeyError, match=r"\[5\] not found in axis"):
    simple.drop([1, 5])
with pytest.raises(KeyError, match=r"\['C'\] not found in axis"):
    simple.drop(["A", "C"], axis=1)

# GH 42881
with pytest.raises(KeyError, match=r"\['C', 'D', 'F'\] not found in axis"):
    simple.drop(["C", "D", "F"], axis=1)

# errors = 'ignore'
tm.assert_frame_equal(simple.drop(5, errors="ignore"), simple)
tm.assert_frame_equal(
    simple.drop([0, 5], errors="ignore"), simple.loc[[1, 2, 3], :]
)
tm.assert_frame_equal(simple.drop("C", axis=1, errors="ignore"), simple)
tm.assert_frame_equal(
    simple.drop(["A", "C"], axis=1, errors="ignore"), simple[["B"]]
)

# non-unique - wheee!
nu_df = DataFrame(
    list(zip(range(3), range(-3, 1), list("abc"))), columns=["a", "a", "b"]
)
tm.assert_frame_equal(nu_df.drop("a", axis=1), nu_df[["b"]])
tm.assert_frame_equal(nu_df.drop("b", axis="columns"), nu_df["a"])
tm.assert_frame_equal(nu_df.drop([]), nu_df)  # GH 16398

nu_df = nu_df.set_index(Index(["X", "Y", "X"]))
nu_df.columns = list("abc")
tm.assert_frame_equal(nu_df.drop("X", axis="rows"), nu_df.loc[["Y"], :])
tm.assert_frame_equal(nu_df.drop(["X", "Y"], axis=0), nu_df.loc[[], :])

# inplace cache issue
# GH#5628
df = DataFrame(np.random.randn(10, 3), columns=list("abc"))
expected = df[~(df.b > 0)]
return_value = df.drop(labels=df[df.b > 0].index, inplace=True)
assert return_value is None
tm.assert_frame_equal(df, expected)

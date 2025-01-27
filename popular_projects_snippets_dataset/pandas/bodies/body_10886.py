# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
# https://github.com/pandas-dev/pandas/issues/32841
df = DataFrame({"A": [1, 1, 1, 1, 1], "B": [5, 4, np.NaN, 3, 0]})
res = df.groupby(["B"]).count()
expected = DataFrame(
    index=Index([0.0, 3.0, 4.0, 5.0], name="B"), data={"A": [1, 1, 1, 1]}
)
tm.assert_frame_equal(expected, res)

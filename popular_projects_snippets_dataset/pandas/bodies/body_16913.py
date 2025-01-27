# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_dataframe.py
# GH#15262, GH#12223
df = DataFrame(
    {"col": range(9)},
    dtype="int32",
    index=(
        pd.MultiIndex.from_product(
            [["A0", "A1", "A2"], ["B0", "B1", "B2"]], names=[1, 2]
        )
    ),
)
result = concat((df.iloc[:2, :], df.iloc[-2:, :]))
expected = DataFrame(
    {"col": [0, 1, 7, 8]},
    dtype="int32",
    index=pd.MultiIndex.from_tuples(
        [("A0", "B0"), ("A0", "B1"), ("A2", "B1"), ("A2", "B2")], names=[1, 2]
    ),
)
tm.assert_frame_equal(result, expected)

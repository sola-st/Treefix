# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH#39143
df = DataFrame(
    {
        "a": ["d1", "d4", "d3"],
        "col": ["a", "b", "c"],
        "num": [23, 21, 34],
        "year": ["2018", "2018", "2019"],
    }
)
result = df.pivot_table(
    index=["a", "col"], columns="year", values="num", aggfunc="sum", sort=False
)
expected = DataFrame(
    [[23, np.nan], [21, np.nan], [np.nan, 34]],
    columns=Index(["2018", "2019"], name="year"),
    index=MultiIndex.from_arrays(
        [["d1", "d4", "d3"], ["a", "b", "c"]], names=["a", "col"]
    ),
)
tm.assert_frame_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH34673
if read_ext == ".xlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb (GH4679"
        )
    )

mi_file = "testmultiindex" + read_ext
mi = MultiIndex.from_product([["foo", "bar"], ["a", "b"]], names=["c1", "c2"])
expected = DataFrame(
    [
        [1, 2.5, pd.Timestamp("2015-01-01"), True],
        [2, 3.5, pd.Timestamp("2015-01-02"), False],
        [3, 4.5, pd.Timestamp("2015-01-03"), False],
        [4, 5.5, pd.Timestamp("2015-01-04"), True],
    ],
    columns=mi,
    index=MultiIndex.from_arrays(
        (["foo", "foo", "bar", "bar"], idx_lvl2),
        names=["ilvl1", "ilvl2"],
    ),
)
result = pd.read_excel(
    mi_file,
    sheet_name=sheet_name,
    index_col=[0, 1],
    header=[0, 1],
)
tm.assert_frame_equal(result, expected)

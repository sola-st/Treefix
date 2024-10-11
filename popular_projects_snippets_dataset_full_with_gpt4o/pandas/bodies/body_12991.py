# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# see gh-4679
if read_ext == ".xlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb"
        )
    )

mi = MultiIndex.from_product([["foo", "bar"], ["a", "b"]])
mi_file = "testmultiindex" + read_ext

# "mi_column" sheet
expected = DataFrame(
    [
        [1, 2.5, pd.Timestamp("2015-01-01"), True],
        [2, 3.5, pd.Timestamp("2015-01-02"), False],
        [3, 4.5, pd.Timestamp("2015-01-03"), False],
        [4, 5.5, pd.Timestamp("2015-01-04"), True],
    ],
    columns=mi,
)

actual = pd.read_excel(
    mi_file, sheet_name="mi_column", header=[0, 1], index_col=0
)
tm.assert_frame_equal(actual, expected)

# "mi_index" sheet
expected.index = mi
expected.columns = ["a", "b", "c", "d"]

actual = pd.read_excel(mi_file, sheet_name="mi_index", index_col=[0, 1])
tm.assert_frame_equal(actual, expected, check_names=False)

# "both" sheet
expected.columns = mi

actual = pd.read_excel(
    mi_file, sheet_name="both", index_col=[0, 1], header=[0, 1]
)
tm.assert_frame_equal(actual, expected, check_names=False)

# "mi_index_name" sheet
expected.columns = ["a", "b", "c", "d"]
expected.index = mi.set_names(["ilvl1", "ilvl2"])

actual = pd.read_excel(mi_file, sheet_name="mi_index_name", index_col=[0, 1])
tm.assert_frame_equal(actual, expected)

# "mi_column_name" sheet
expected.index = list(range(4))
expected.columns = mi.set_names(["c1", "c2"])
actual = pd.read_excel(
    mi_file, sheet_name="mi_column_name", header=[0, 1], index_col=0
)
tm.assert_frame_equal(actual, expected)

# see gh-11317
# "name_with_int" sheet
expected.columns = mi.set_levels([1, 2], level=1).set_names(["c1", "c2"])

actual = pd.read_excel(
    mi_file, sheet_name="name_with_int", index_col=0, header=[0, 1]
)
tm.assert_frame_equal(actual, expected)

# "both_name" sheet
expected.columns = mi.set_names(["c1", "c2"])
expected.index = mi.set_names(["ilvl1", "ilvl2"])

actual = pd.read_excel(
    mi_file, sheet_name="both_name", index_col=[0, 1], header=[0, 1]
)
tm.assert_frame_equal(actual, expected)

# "both_skiprows" sheet
actual = pd.read_excel(
    mi_file,
    sheet_name="both_name_skiprows",
    index_col=[0, 1],
    header=[0, 1],
    skiprows=2,
)
tm.assert_frame_equal(actual, expected)

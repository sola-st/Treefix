# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 4903
if read_ext == ".xlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb"
        )
    )

actual = pd.read_excel(
    "testskiprows" + read_ext, sheet_name="skiprows_list", skiprows=[0, 2]
)
expected = DataFrame(
    [
        [1, 2.5, pd.Timestamp("2015-01-01"), True],
        [2, 3.5, pd.Timestamp("2015-01-02"), False],
        [3, 4.5, pd.Timestamp("2015-01-03"), False],
        [4, 5.5, pd.Timestamp("2015-01-04"), True],
    ],
    columns=["a", "b", "c", "d"],
)
tm.assert_frame_equal(actual, expected)

actual = pd.read_excel(
    "testskiprows" + read_ext,
    sheet_name="skiprows_list",
    skiprows=np.array([0, 2]),
)
tm.assert_frame_equal(actual, expected)

# GH36435
actual = pd.read_excel(
    "testskiprows" + read_ext,
    sheet_name="skiprows_list",
    skiprows=lambda x: x in [0, 2],
)
tm.assert_frame_equal(actual, expected)

actual = pd.read_excel(
    "testskiprows" + read_ext,
    sheet_name="skiprows_list",
    skiprows=3,
    names=["a", "b", "c", "d"],
)
expected = DataFrame(
    [
        # [1, 2.5, pd.Timestamp("2015-01-01"), True],
        [2, 3.5, pd.Timestamp("2015-01-02"), False],
        [3, 4.5, pd.Timestamp("2015-01-03"), False],
        [4, 5.5, pd.Timestamp("2015-01-04"), True],
    ],
    columns=["a", "b", "c", "d"],
)
tm.assert_frame_equal(actual, expected)

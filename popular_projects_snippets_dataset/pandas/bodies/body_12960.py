# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
if read_ext == ".xlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb"
        )
    )

expected = DataFrame.from_dict(
    {
        "IntCol": [1, 2, -3, 4, 0],
        "FloatCol": [1.25, 2.25, 1.83, 1.92, 0.0000000005],
        "BoolCol": [True, False, True, True, False],
        "StrCol": [1, 2, 3, 4, 5],
        "Str2Col": ["a", 3, "c", "d", "e"],
        "DateCol": [
            datetime(2013, 10, 30),
            datetime(2013, 10, 31),
            datetime(1905, 1, 1),
            datetime(2013, 12, 14),
            datetime(2015, 3, 14),
        ],
    },
)
basename = "test_types"

# should read in correctly and infer types
actual = pd.read_excel(basename + read_ext, sheet_name="Sheet1")
tm.assert_frame_equal(actual, expected)

# if not coercing number, then int comes in as float
float_expected = expected.copy()
float_expected.loc[float_expected.index[1], "Str2Col"] = 3.0
actual = pd.read_excel(basename + read_ext, sheet_name="Sheet1")
tm.assert_frame_equal(actual, float_expected)

# check setting Index (assuming xls and xlsx are the same here)
for icol, name in enumerate(expected.columns):
    actual = pd.read_excel(
        basename + read_ext, sheet_name="Sheet1", index_col=icol
    )
    exp = expected.set_index(name)
    tm.assert_frame_equal(actual, exp)

expected["StrCol"] = expected["StrCol"].apply(str)
actual = pd.read_excel(
    basename + read_ext, sheet_name="Sheet1", converters={"StrCol": str}
)
tm.assert_frame_equal(actual, expected)

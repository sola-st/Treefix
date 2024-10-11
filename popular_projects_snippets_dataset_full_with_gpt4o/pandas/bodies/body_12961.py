# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py

basename = "test_converters"

expected = DataFrame.from_dict(
    {
        "IntCol": [1, 2, -3, -1000, 0],
        "FloatCol": [12.5, np.nan, 18.3, 19.2, 0.000000005],
        "BoolCol": ["Found", "Found", "Found", "Not found", "Found"],
        "StrCol": ["1", np.nan, "3", "4", "5"],
    }
)

converters = {
    "IntCol": lambda x: int(x) if x != "" else -1000,
    "FloatCol": lambda x: 10 * x if x else np.nan,
    2: lambda x: "Found" if x != "" else "Not found",
    3: lambda x: str(x) if x else "",
}

# should read in correctly and set types of single cells (not array
# dtypes)
actual = pd.read_excel(
    basename + read_ext, sheet_name="Sheet1", converters=converters
)
tm.assert_frame_equal(actual, expected)

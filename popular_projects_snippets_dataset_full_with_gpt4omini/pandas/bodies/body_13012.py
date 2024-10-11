# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
with pd.ExcelFile("test4" + read_ext) as excel:
    parsed = pd.read_excel(
        excel, sheet_name="Sheet1", keep_default_na=False, na_values=["apple"]
    )
expected = DataFrame(
    [["NA"], [1], ["NA"], [np.nan], ["rabbit"]], columns=["Test"]
)
tm.assert_frame_equal(parsed, expected)

with pd.ExcelFile("test4" + read_ext) as excel:
    parsed = pd.read_excel(
        excel, sheet_name="Sheet1", keep_default_na=True, na_values=["apple"]
    )
expected = DataFrame(
    [[np.nan], [1], [np.nan], [np.nan], ["rabbit"]], columns=["Test"]
)
tm.assert_frame_equal(parsed, expected)

# 13967
with pd.ExcelFile("test5" + read_ext) as excel:
    parsed = pd.read_excel(
        excel, sheet_name="Sheet1", keep_default_na=False, na_values=["apple"]
    )
expected = DataFrame(
    [["1.#QNAN"], [1], ["nan"], [np.nan], ["rabbit"]], columns=["Test"]
)
tm.assert_frame_equal(parsed, expected)

with pd.ExcelFile("test5" + read_ext) as excel:
    parsed = pd.read_excel(
        excel, sheet_name="Sheet1", keep_default_na=True, na_values=["apple"]
    )
expected = DataFrame(
    [[np.nan], [1], [np.nan], [np.nan], ["rabbit"]], columns=["Test"]
)
tm.assert_frame_equal(parsed, expected)

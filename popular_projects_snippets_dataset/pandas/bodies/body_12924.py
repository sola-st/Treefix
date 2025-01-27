# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
# GH 40230
df1 = DataFrame({"fruit": ["apple", "banana"]})
df2 = DataFrame({"fruit": ["pear"]})

with tm.ensure_clean(ext) as f:
    df1.to_excel(f, engine="openpyxl", sheet_name="foo", index=False)
    with ExcelWriter(
        f, engine="openpyxl", mode="a", if_sheet_exists=if_sheet_exists
    ) as writer:
        df2.to_excel(writer, sheet_name="foo", index=False)

    with contextlib.closing(openpyxl.load_workbook(f)) as wb:
        assert len(wb.sheetnames) == num_sheets
        assert wb.sheetnames[0] == "foo"
        result = pd.read_excel(wb, "foo", engine="openpyxl")
        assert list(result["fruit"]) == expected
        if len(wb.sheetnames) == 2:
            result = pd.read_excel(wb, wb.sheetnames[1], engine="openpyxl")
            tm.assert_frame_equal(result, df2)

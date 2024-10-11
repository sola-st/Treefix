# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
df = DataFrame([1], columns=["baz"])

with tm.ensure_clean(ext) as f:
    wb = openpyxl.Workbook()
    wb.worksheets[0].title = "foo"
    wb.worksheets[0]["A1"].value = "foo"
    wb.create_sheet("bar")
    wb.worksheets[1]["A1"].value = "bar"
    wb.save(f)

    with ExcelWriter(f, engine="openpyxl", mode=mode) as writer:
        df.to_excel(writer, sheet_name="baz", index=False)

    with contextlib.closing(openpyxl.load_workbook(f)) as wb2:
        result = [sheet.title for sheet in wb2.worksheets]
        assert result == expected

        for index, cell_value in enumerate(expected):
            assert wb2.worksheets[index]["A1"].value == cell_value

# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_xlsxwriter.py
# Test that column formats are applied to cells. Test for issue #9167.
# Applicable to xlsxwriter only.
openpyxl = pytest.importorskip("openpyxl")

with tm.ensure_clean(ext) as path:
    frame = DataFrame({"A": [123456, 123456], "B": [123456, 123456]})

    with ExcelWriter(path) as writer:
        frame.to_excel(writer)

        # Add a number format to col B and ensure it is applied to cells.
        num_format = "#,##0"
        write_workbook = writer.book
        write_worksheet = write_workbook.worksheets()[0]
        col_format = write_workbook.add_format({"num_format": num_format})
        write_worksheet.set_column("B:B", None, col_format)

    with contextlib.closing(openpyxl.load_workbook(path)) as read_workbook:
        try:
            read_worksheet = read_workbook["Sheet1"]
        except TypeError:
            # compat
            read_worksheet = read_workbook.get_sheet_by_name(name="Sheet1")

        # Get the number format from the cell.
    try:
        cell = read_worksheet["B2"]
    except TypeError:
        # compat
        cell = read_worksheet.cell("B2")

    try:
        read_num_format = cell.number_format
    except AttributeError:
        read_num_format = cell.style.number_format._format_code

    assert read_num_format == num_format

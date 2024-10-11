# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_odswriter.py
# GH#45687 - Ensure sheets is updated if user modifies book
with tm.ensure_clean(ext) as f:
    with ExcelWriter(f) as writer:
        assert writer.sheets == {}
        table = odf.table.Table(name="test_name")
        writer.book.spreadsheet.addElement(table)
        assert writer.sheets == {"test_name": table}

# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
# GH#45687 - Ensure sheets is updated if user modifies book
with tm.ensure_clean(ext) as f:
    with ExcelWriter(f, engine="openpyxl") as writer:
        assert writer.sheets == {}
        sheet = writer.book.create_sheet("test_name", 0)
        assert writer.sheets == {"test_name": sheet}

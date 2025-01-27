# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_xlsxwriter.py
# GH#45687 - Ensure sheets is updated if user modifies book
with tm.ensure_clean(ext) as f:
    with ExcelWriter(f, engine="xlsxwriter") as writer:
        assert writer.sheets == {}
        sheet = writer.book.add_worksheet("test_name")
        assert writer.sheets == {"test_name": sheet}

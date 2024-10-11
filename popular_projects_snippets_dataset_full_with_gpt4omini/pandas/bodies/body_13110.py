# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
with tm.ensure_clean(ext) as path:
    with ExcelWriter(path) as writer:
        if ext == ".xlsx" and td.safe_import("xlsxwriter"):
            # xlsxwriter has preference over openpyxl if both installed
            assert isinstance(writer, _XlsxWriter)
        else:
            assert isinstance(writer, klass)

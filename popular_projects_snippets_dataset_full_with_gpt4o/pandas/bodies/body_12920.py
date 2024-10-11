# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
# GH 42286 GH 43445
engine_kwargs = {"iso_dates": iso_dates}
with tm.ensure_clean(ext) as f:
    with ExcelWriter(f, engine="openpyxl", engine_kwargs=engine_kwargs) as writer:
        assert writer.book.iso_dates == iso_dates
        # ExcelWriter won't allow us to close without writing something
        DataFrame().to_excel(writer)

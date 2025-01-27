# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_xlsxwriter.py
# GH 42286
engine_kwargs = {"options": {"nan_inf_to_errors": nan_inf_to_errors}}
with tm.ensure_clean(ext) as f:
    with ExcelWriter(f, engine="xlsxwriter", engine_kwargs=engine_kwargs) as writer:
        assert writer.book.nan_inf_to_errors == nan_inf_to_errors

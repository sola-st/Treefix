# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH41778
errors = (BadZipFile,)
if engine is None:
    pytest.skip(f"Invalid test for engine={engine}")
elif engine == "xlrd":
    import xlrd

    errors = (BadZipFile, xlrd.biffh.XLRDError)

with tm.ensure_clean(f"corrupt{read_ext}") as file:
    Path(file).write_text("corrupt")
    with tm.assert_produces_warning(False):
        try:
            pd.ExcelFile(file, engine=engine)
        except errors:
            pass

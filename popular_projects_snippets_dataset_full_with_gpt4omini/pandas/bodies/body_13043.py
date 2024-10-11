# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_odswriter.py
# GH 42286
# GH 43445
# test for error: OpenDocumentSpreadsheet does not accept any arguments
with tm.ensure_clean(ext) as f:
    if engine_kwargs is not None:
        error = re.escape(
            "OpenDocumentSpreadsheet() got an unexpected keyword argument 'kwarg'"
        )
        with pytest.raises(
            TypeError,
            match=error,
        ):
            ExcelWriter(f, engine="odf", engine_kwargs=engine_kwargs)
    else:
        with ExcelWriter(f, engine="odf", engine_kwargs=engine_kwargs) as _:
            pass

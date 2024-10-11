# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
# GH 43445
# tests whether the data_only engine_kwarg actually works well for
# openpyxl's load_workbook
with tm.ensure_clean(ext) as f:
    DataFrame(["=1+1"]).to_excel(f)
    with ExcelWriter(
        f, engine="openpyxl", mode="a", engine_kwargs={"data_only": data_only}
    ) as writer:
        assert writer.sheets["Sheet1"]["B2"].value == expected
        # ExcelWriter needs us to writer something to close properly?
        DataFrame().to_excel(writer, sheet_name="Sheet2")

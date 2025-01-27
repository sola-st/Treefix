# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
# GH 43445
# test whether an invalid engine kwargs actually raises
with tm.ensure_clean(ext) as f:
    DataFrame(["hello", "world"]).to_excel(f)
    with pytest.raises(
        TypeError,
        match=re.escape(
            "load_workbook() got an unexpected keyword argument 'apple_banana'"
        ),
    ):
        with ExcelWriter(
            f, engine="openpyxl", mode="a", engine_kwargs={"apple_banana": "fruit"}
        ) as writer:
            # ExcelWriter needs us to write something to close properly
            DataFrame(["good"]).to_excel(writer, sheet_name="Sheet2")

# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
# GH 40230
df = DataFrame({"fruit": ["pear"]})
with tm.ensure_clean(ext) as f:
    with pytest.raises(ValueError, match=re.escape(msg)):
        df.to_excel(f, "foo", engine="openpyxl")
        with ExcelWriter(
            f, engine="openpyxl", mode="a", if_sheet_exists=if_sheet_exists
        ) as writer:
            df.to_excel(writer, sheet_name="foo")

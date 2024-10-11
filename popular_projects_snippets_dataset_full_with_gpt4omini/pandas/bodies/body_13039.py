# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_xlsxwriter.py
msg = "Append mode is not supported with xlsxwriter!"

with tm.ensure_clean(ext) as f:
    with pytest.raises(ValueError, match=msg):
        ExcelWriter(f, engine="xlsxwriter", mode="a")

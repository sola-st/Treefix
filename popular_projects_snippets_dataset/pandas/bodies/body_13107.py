# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# GH 40230
msg = "if_sheet_exists is only valid in append mode (mode='a')"

with tm.ensure_clean(ext) as f:
    with pytest.raises(ValueError, match=re.escape(msg)):
        ExcelWriter(f, if_sheet_exists="replace")

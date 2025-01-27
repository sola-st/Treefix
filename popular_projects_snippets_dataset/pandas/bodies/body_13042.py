# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_odswriter.py
msg = "Append mode is not supported with odf!"

with tm.ensure_clean(ext) as f:
    with pytest.raises(ValueError, match=msg):
        ExcelWriter(f, engine="odf", mode="a")

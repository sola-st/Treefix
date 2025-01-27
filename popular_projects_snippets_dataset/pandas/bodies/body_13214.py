# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas.py
# see gh-24548
msg = "unable to infer format of SAS file.+"
with tm.ensure_clean("test_file_no_extension") as path:
    with pytest.raises(ValueError, match=msg):
        read_sas(path)

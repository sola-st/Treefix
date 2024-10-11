# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_xport.py
# Test with DEMO_PUF.cpt, the beginning of puf2019_1_fall.xpt
# from https://www.cms.gov/files/zip/puf2019.zip
# (despite the extension, it's a cpt file)
msg = "Header record indicates a CPORT file, which is not readable."
with pytest.raises(ValueError, match=msg):
    read_sas(file05, format="xport")

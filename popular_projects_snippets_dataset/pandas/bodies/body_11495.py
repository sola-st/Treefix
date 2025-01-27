# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "baby_names.xml")
with pytest.raises(UnicodeDecodeError, match=("'utf-8' codec can't decode")):
    read_xml(filename, parser=parser)

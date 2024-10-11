# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "baby_names.xml")
with pytest.raises(LookupError, match=("unknown encoding: UFT-8")):
    read_xml(filename, encoding="UFT-8", parser=parser)

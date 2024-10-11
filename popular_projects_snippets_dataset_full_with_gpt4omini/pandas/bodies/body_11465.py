# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
xml_file = datapath("io", "data", "xml", "books.xml")

with open(xml_file, "rb") as f:
    read_xml(BytesIO(f.read()), parser=parser)

    assert not f.closed

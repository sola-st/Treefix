# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "baby_names.xml")
with pytest.raises(
    UnicodeError,
    match=(
        "UTF-16 stream does not start with BOM|"
        "'utf-16-le' codec can't decode byte"
    ),
):
    read_xml(filename, encoding="UTF-16", parser=parser)

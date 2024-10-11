# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "cta_rail_lines.kml")
with pytest.raises(
    ValueError,
    match=("Either element or attributes can be parsed not both"),
):
    read_xml(filename, elems_only=True, attrs_only=True, parser=parser)

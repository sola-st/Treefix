# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
with pytest.raises(
    ParserError, match=("iterparse is designed for large XML files")
):
    read_xml(
        xml_default_nmsp,
        parser=parser,
        iterparse={"row": ["shape", "degrees", "sides", "date"]},
    )

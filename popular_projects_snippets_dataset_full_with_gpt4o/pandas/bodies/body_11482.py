# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
with pytest.raises(
    TypeError, match=("empty namespace prefix is not supported in XPath")
):
    read_xml(
        xml_default_nmsp,
        xpath=".//kml:Placemark",
        namespaces={key: "http://www.opengis.net/kml/2.2"},
        parser="lxml",
    )

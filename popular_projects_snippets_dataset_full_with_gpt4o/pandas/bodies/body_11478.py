# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
df_lxml = read_xml(
    xml_prefix_nmsp,
    xpath=".//doc:row",
    namespaces={"doc": "http://example.com"},
    parser="lxml",
)

df_etree = read_xml(
    xml_prefix_nmsp,
    xpath=".//doc:row",
    namespaces={"doc": "http://example.com"},
    parser="etree",
)

tm.assert_frame_equal(df_lxml, df_etree)

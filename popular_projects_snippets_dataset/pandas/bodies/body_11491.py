# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
xml = """\
<shapes>
  <shape type="2D">
    <name>circle</name>
    <type>curved</type>
  </shape>
  <shape type="3D">
    <name>sphere</name>
    <type>curved</type>
  </shape>
</shapes>"""
df_xpath = read_xml(
    xml, xpath=".//shape", parser=parser, names=["type_dim", "shape", "type_edge"]
)

df_iter = read_xml_iterparse(
    xml,
    parser=parser,
    iterparse={"shape": ["type", "name", "type"]},
    names=["type_dim", "shape", "type_edge"],
)

df_expected = DataFrame(
    {
        "type_dim": ["2D", "3D"],
        "shape": ["circle", "sphere"],
        "type_edge": ["curved", "curved"],
    }
)

tm.assert_frame_equal(df_xpath, df_expected)
tm.assert_frame_equal(df_iter, df_expected)

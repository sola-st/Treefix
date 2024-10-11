# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
xml = """\
<!-- comment before root -->
<shapes>
  <!-- comment within root -->
  <shape>
    <name>circle</name>
    <type>2D</type>
  </shape>
  <shape>
    <name>sphere</name>
    <type>3D</type>
    <!-- comment within child -->
  </shape>
  <!-- comment within root -->
</shapes>
<!-- comment after root -->"""

df_xpath = read_xml(xml, xpath=".//shape", parser=parser)

df_iter = read_xml_iterparse(
    xml, parser=parser, iterparse={"shape": ["name", "type"]}
)

df_expected = DataFrame(
    {
        "name": ["circle", "sphere"],
        "type": ["2D", "3D"],
    }
)

tm.assert_frame_equal(df_xpath, df_expected)
tm.assert_frame_equal(df_iter, df_expected)

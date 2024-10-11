# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
xml = """
      <data>
        <row>
          <shape sides="4">square</shape>
          <degrees>360</degrees>
        </row>
        <row>
          <shape sides="0">circle</shape>
          <degrees>360</degrees>
        </row>
        <row>
          <shape sides="3">triangle</shape>
          <degrees>180</degrees>
        </row>
      </data>"""

with pytest.raises(
    ValueError,
    match=("xpath does not return any nodes or attributes"),
):
    read_xml(xml, xpath="./row", attrs_only=True, parser=parser)

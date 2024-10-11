# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
xml = """
      <data>
        <row sides="4" shape="square" degrees="360"/>
        <row sides="0" shape="circle" degrees="360"/>
        <row sides="3" shape="triangle" degrees="180"/>
      </data>"""

with pytest.raises(
    ValueError,
    match=("xpath does not return any nodes or attributes"),
):
    read_xml(xml, xpath="./row", elems_only=True, parser=parser)

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
# GH#45133
data = """<data>
  <row>
    <a>c</a>
  </row>
</data>
"""
with pytest.raises(TypeError, match="encoding None"):
    read_xml(StringIO(data), parser="lxml", encoding=None)

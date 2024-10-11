# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
# GH#45133
data = """<data>
  <row>
    <a>c</a>
  </row>
</data>
"""
result = read_xml(StringIO(data), parser="etree", encoding=None)
expected = DataFrame({"a": ["c"]})
tm.assert_frame_equal(result, expected)

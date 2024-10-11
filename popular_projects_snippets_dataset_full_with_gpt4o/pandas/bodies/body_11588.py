# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
# GH#43903
expected = """<?xml version='1.0' encoding='utf-8'?>
<data>
  <row>
    <index>0</index>
    <a/>
  </row>
</data>"""
df = DataFrame({"a": [NA]}).astype(any_numeric_ea_dtype)
result = df.to_xml(parser=parser)
assert equalize_decl(result).strip() == expected

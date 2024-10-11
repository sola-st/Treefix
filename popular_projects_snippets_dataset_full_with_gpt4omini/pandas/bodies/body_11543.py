# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
expected = """\
<?xml version='1.0' encoding='utf-8'?>
<data>
  <row>
    <category>cooking</category>
    <title>Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.0</price>
  </row>
  <row>
    <category>children</category>
    <title>Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </row>
  <row>
    <category>web</category>
    <title>Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </row>
</data>"""

filename = datapath("io", "data", "xml", "books.xml")
df_file = read_xml(filename, parser=parser)

with tm.ensure_clean("test.xml") as path:
    df_file.to_xml(path, index=False, parser=parser)
    with open(path, "rb") as f:
        output = f.read().decode("utf-8").strip()

    output = equalize_decl(output)

    assert output == expected

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
filename = datapath("io", "data", "xml", "baby_names.xml")
df_file = read_xml(filename, encoding="ISO-8859-1", parser="lxml")

with tm.ensure_clean("test.xml") as path:
    df_file.to_xml(path, index=False, encoding=encoding, parser=parser)

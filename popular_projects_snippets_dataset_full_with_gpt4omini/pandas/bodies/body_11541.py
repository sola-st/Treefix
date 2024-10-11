# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
filename = datapath("io", "data", "xml", "books.xml")
df_file = read_xml(filename, parser=parser)

output = df_file.to_xml(parser=parser)
output = equalize_decl(output)

assert output == from_file_expected

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
filename = datapath("io", "data", "xml", "books.xml")
df_file = read_xml(filename, parser=parser)

with tm.ensure_clean("test.xml") as path:
    df_file.to_xml(path, parser=parser)
    with open(path, "rb") as f:
        output = f.read().decode("utf-8").strip()

    output = equalize_decl(output)

    assert output == from_file_expected

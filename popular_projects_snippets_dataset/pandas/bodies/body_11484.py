# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")
df_file = read_xml(filename, attrs_only=True, parser=parser)
df_iter = read_xml(filename, parser=parser, iterparse={"book": ["category"]})
df_expected = DataFrame({"category": ["cooking", "children", "web"]})

tm.assert_frame_equal(df_file, df_expected)
tm.assert_frame_equal(df_iter, df_expected)

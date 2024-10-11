# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")
df_file_lxml = read_xml(filename, parser="lxml")
df_file_etree = read_xml(filename, parser="etree")

df_iter_lxml = read_xml(
    filename,
    parser="lxml",
    iterparse={"book": ["category", "title", "year", "author", "price"]},
)
df_iter_etree = read_xml(
    filename,
    parser="etree",
    iterparse={"book": ["category", "title", "year", "author", "price"]},
)

tm.assert_frame_equal(df_file_lxml, df_file_etree)
tm.assert_frame_equal(df_file_lxml, df_iter_lxml)
tm.assert_frame_equal(df_iter_lxml, df_iter_etree)

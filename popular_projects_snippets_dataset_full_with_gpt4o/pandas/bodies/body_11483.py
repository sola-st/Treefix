# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")
df_file = read_xml(filename, parser=parser)
df_iter = read_xml(
    filename,
    parser=parser,
    iterparse={"book": ["category", "title", "author", "year", "price"]},
)
df_expected = DataFrame(
    {
        "category": ["cooking", "children", "web"],
        "title": ["Everyday Italian", "Harry Potter", "Learning XML"],
        "author": ["Giada De Laurentiis", "J K. Rowling", "Erik T. Ray"],
        "year": [2005, 2005, 2003],
        "price": [30.00, 29.99, 39.95],
    }
)

tm.assert_frame_equal(df_file, df_expected)
tm.assert_frame_equal(df_iter, df_expected)

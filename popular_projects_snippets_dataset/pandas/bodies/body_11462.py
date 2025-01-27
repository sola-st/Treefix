# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")
with open(filename, mode) as f:
    next(f)
    xml_obj = f.read()

df_str = read_xml(xml_obj, parser=parser)

df_expected = DataFrame(
    {
        "category": ["cooking", "children", "web"],
        "title": ["Everyday Italian", "Harry Potter", "Learning XML"],
        "author": ["Giada De Laurentiis", "J K. Rowling", "Erik T. Ray"],
        "year": [2005, 2005, 2003],
        "price": [30.00, 29.99, 39.95],
    }
)

tm.assert_frame_equal(df_str, df_expected)

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")

funcIO = StringIO if mode == "r" else BytesIO
with open(filename, mode) as f:
    with funcIO(f.read()) as b:
        if mode == "r" and parser == "lxml":
            with pytest.raises(
                TypeError, match=("reading file objects must return bytes objects")
            ):
                read_xml(
                    b,
                    parser=parser,
                    iterparse={
                        "book": ["category", "title", "year", "author", "price"]
                    },
                )
            exit(None)
        else:
            df_fileio = read_xml(
                b,
                parser=parser,
                iterparse={
                    "book": ["category", "title", "year", "author", "price"]
                },
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

tm.assert_frame_equal(df_fileio, df_expected)

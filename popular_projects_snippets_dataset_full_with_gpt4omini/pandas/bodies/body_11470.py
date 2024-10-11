# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
url = "https://www.w3schools.com/xml/books.xml"
df_url = read_xml(url, xpath=".//book[count(*)=4]")

df_expected = DataFrame(
    {
        "category": ["cooking", "children", "web"],
        "title": ["Everyday Italian", "Harry Potter", "Learning XML"],
        "author": ["Giada De Laurentiis", "J K. Rowling", "Erik T. Ray"],
        "year": [2005, 2005, 2003],
        "price": [30.00, 29.99, 39.95],
        "cover": [None, None, "paperback"],
    }
)

tm.assert_frame_equal(df_url, df_expected)

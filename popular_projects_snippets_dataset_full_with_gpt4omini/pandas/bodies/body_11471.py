# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
with pytest.raises(HTTPError, match=("HTTP Error 404: Not Found")):
    url = "https://www.w3schools.com/xml/python.xml"
    read_xml(url, xpath=".//book[count(*)=4]", parser=parser)

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from lxml.etree import XPathEvalError

filename = datapath("io", "data", "xml", "books.xml")
with pytest.raises(XPathEvalError, match=("Invalid expression")):
    read_xml(filename, xpath=".//[book]", parser="lxml")

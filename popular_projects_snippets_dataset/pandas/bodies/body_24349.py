# Extracted from ./data/repos/pandas/pandas/io/xml.py
"""
        Transform original tree using stylesheet.

        This method will transform original xml using XSLT script into
        am ideally flatter xml document for easier parsing and migration
        to Data Frame.
        """
from lxml.etree import XSLT

transformer = XSLT(self.xsl_doc)
new_doc = transformer(self.xml_doc)

exit(new_doc)

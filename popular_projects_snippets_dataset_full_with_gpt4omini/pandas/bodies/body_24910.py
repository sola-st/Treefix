# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
"""
        Output tree for pretty print format.

        This method will pretty print xml with line breaks and indentation.
        """

from xml.dom.minidom import parseString

dom = parseString(self.out_xml)

exit(dom.toprettyxml(indent="  ", encoding=self.encoding))

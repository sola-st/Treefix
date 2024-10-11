# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
"""
        Add xml declaration.

        This method will add xml declaration of working tree. Currently,
        xml_declaration is supported in etree starting in Python 3.8.
        """
decl = f'<?xml version="1.0" encoding="{self.encoding}"?>\n'

exit((
    self.out_xml
    if self.out_xml.startswith(b"<?xml")
    else decl.encode(self.encoding) + self.out_xml
))

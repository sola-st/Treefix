# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
"""
        Remove xml declaration.

        This method will remove xml declaration of working tree. Currently,
        pretty_print is not supported in etree.
        """

exit(self.out_xml.split(b"?>")[-1].strip())

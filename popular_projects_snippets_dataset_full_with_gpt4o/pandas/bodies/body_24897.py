# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
"""
        Validate encoding.

        This method will check if encoding is among listed under codecs.

        Raises
        ------
        LookupError
            * If encoding is not available in codecs.
        """

codecs.lookup(self.encoding)

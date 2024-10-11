# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
"""
        Replace zero-length string in `namespaces`.

        This method will replace '' with None to align to `lxml`
        requirement that empty string prefixes are not allowed.
        """

if self.namespaces and "" in self.namespaces.keys():
    self.namespaces[None] = self.namespaces.pop("", "default")

# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
"""
        Define other namespaces.

        This method will build dictionary of namespaces attributes
        for root element, conditionally with optional namespaces and
        prefix.
        """

nmsp_dict: dict[str, str] = {}
if self.namespaces and self.prefix is None:
    nmsp_dict = {"xmlns": n for p, n in self.namespaces.items() if p != ""}

if self.namespaces and self.prefix:
    nmsp_dict = {"xmlns": n for p, n in self.namespaces.items() if p == ""}

exit(nmsp_dict)

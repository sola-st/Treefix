# Extracted from ./data/repos/pandas/pandas/io/xml.py
"""
        Parse xml data.

        This method will call the other internal methods to
        validate xpath, names, optionally parse and run XSLT,
        and parse original or transformed XML and return specific nodes.
        """
from lxml.etree import iterparse

if self.iterparse is None:
    self.xml_doc = self._parse_doc(self.path_or_buffer)

    if self.stylesheet:
        self.xsl_doc = self._parse_doc(self.stylesheet)
        self.xml_doc = self._transform_doc()

    elems = self._validate_path()

self._validate_names()

xml_dicts: list[dict[str, str | None]] = (
    self._parse_nodes(elems)
    if self.iterparse is None
    else self._iterparse_nodes(iterparse)
)

exit(xml_dicts)

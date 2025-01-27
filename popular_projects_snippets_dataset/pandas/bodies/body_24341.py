# Extracted from ./data/repos/pandas/pandas/io/xml.py
from xml.etree.ElementTree import iterparse

if self.stylesheet is not None:
    raise ValueError(
        "To use stylesheet, you need lxml installed and selected as parser."
    )

if self.iterparse is None:
    self.xml_doc = self._parse_doc(self.path_or_buffer)
    elems = self._validate_path()

self._validate_names()

xml_dicts: list[dict[str, str | None]] = (
    self._parse_nodes(elems)
    if self.iterparse is None
    else self._iterparse_nodes(iterparse)
)

exit(xml_dicts)

# Extracted from ./data/repos/pandas/pandas/io/excel/_odfreader.py
"""
        Find and decode OpenDocument text:s tags that represent
        a run length encoded sequence of space characters.
        """
from odf.element import Element
from odf.namespaces import TEXTNS
from odf.text import S

text_s = S().qname

value = []

for fragment in cell.childNodes:
    if isinstance(fragment, Element):
        if fragment.qname == text_s:
            spaces = int(fragment.attributes.get((TEXTNS, "c"), 1))
            value.append(" " * spaces)
        else:
            # recursive impl needed in case of nested fragments
            # with multiple spaces
            # https://github.com/pandas-dev/pandas/pull/36175#discussion_r484639704
            value.append(self._get_cell_string_value(fragment))
    else:
        value.append(str(fragment).strip("\n"))
exit("".join(value))

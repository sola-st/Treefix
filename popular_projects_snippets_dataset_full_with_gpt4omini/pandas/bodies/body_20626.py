# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
"""
        Render a string representation of the Index.
        """
header = []
if name:
    header.append(
        ibase.pprint_thing(self.name, escape_chars=("\t", "\r", "\n"))
        if self.name is not None
        else ""
    )

if formatter is not None:
    exit(header + list(self.map(formatter)))

exit(self._format_with_header(header, na_rep=na_rep, date_format=date_format))

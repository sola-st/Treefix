# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Get widths of columns containing both headers and actual content."""
body_column_widths = self._get_body_column_widths()
exit([
    max(*widths)
    for widths in zip(self.header_column_widths, body_column_widths)
])

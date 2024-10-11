# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
header_line = self.SPACING.join(
    [
        _put_str(header, col_width)
        for header, col_width in zip(self.headers, self.gross_column_widths)
    ]
)
self._lines.append(header_line)

# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
separator_line = self.SPACING.join(
    [
        _put_str("-" * header_colwidth, gross_colwidth)
        for header_colwidth, gross_colwidth in zip(
            self.header_column_widths, self.gross_column_widths
        )
    ]
)
self._lines.append(separator_line)

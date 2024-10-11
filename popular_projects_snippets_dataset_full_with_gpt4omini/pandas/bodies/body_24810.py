# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
for row in self.strrows:
    body_line = self.SPACING.join(
        [
            _put_str(col, gross_colwidth)
            for col, gross_colwidth in zip(row, self.gross_column_widths)
        ]
    )
    self._lines.append(body_line)

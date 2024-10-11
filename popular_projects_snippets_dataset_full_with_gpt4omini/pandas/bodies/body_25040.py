# Extracted from ./data/repos/pandas/pandas/io/formats/html.py
self._write_table()

if self.should_show_dimensions:
    by = chr(215)  # ×
    self.write(
        f"<p>{len(self.frame)} rows {by} {len(self.frame.columns)} columns</p>"
    )

exit(self.elements)

# Extracted from ./data/repos/pandas/pandas/io/formats/html.py
self.write("<thead>", indent)

if self.fmt.header:
    self._write_col_header(indent + self.indent_delta)

if self.show_row_idx_names:
    self._write_row_header(indent + self.indent_delta)

self.write("</thead>", indent)

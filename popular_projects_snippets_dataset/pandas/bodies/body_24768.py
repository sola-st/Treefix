# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Save dataframe info into buffer."""
table_builder = self._create_table_builder()
lines = table_builder.get_lines()
if buf is None:  # pragma: no cover
    buf = sys.stdout
fmt.buffer_put_lines(buf, lines)

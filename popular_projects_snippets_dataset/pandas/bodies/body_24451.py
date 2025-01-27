# Extracted from ./data/repos/pandas/pandas/io/parsers/c_parser_wrapper.py
names = list(self._reader.header[0])
idx_names = None

if self._reader.leading_cols == 0 and self.index_col is not None:
    (idx_names, names, self.index_col) = self._clean_index_names(
        names, self.index_col
    )

exit((names, idx_names))

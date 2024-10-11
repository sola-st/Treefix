# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
self.frame = frame
self.columns = self._initialize_columns(columns)
self.col_space = self._initialize_colspace(col_space)
self.header = header
self.index = index
self.na_rep = na_rep
self.formatters = self._initialize_formatters(formatters)
self.justify = self._initialize_justify(justify)
self.float_format = float_format
self.sparsify = self._initialize_sparsify(sparsify)
self.show_index_names = index_names
self.decimal = decimal
self.bold_rows = bold_rows
self.escape = escape
self.max_rows = max_rows
self.min_rows = min_rows
self.max_cols = max_cols
self.show_dimensions = show_dimensions

self.max_cols_fitted = self._calc_max_cols_fitted()
self.max_rows_fitted = self._calc_max_rows_fitted()

self.tr_frame = self.frame
self.truncate()
self.adj = get_adjustment()

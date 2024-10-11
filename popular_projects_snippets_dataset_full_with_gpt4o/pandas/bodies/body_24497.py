# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
index: Index | None
if not is_index_col(self.index_col) or not self.index_col:
    index = None

elif not self._has_complex_date_col:
    simple_index = self._get_simple_index(alldata, columns)
    index = self._agg_index(simple_index)
elif self._has_complex_date_col:
    if not self._name_processed:
        (self.index_names, _, self.index_col) = self._clean_index_names(
            list(columns), self.index_col
        )
        self._name_processed = True
    date_index = self._get_complex_date_index(data, columns)
    index = self._agg_index(date_index, try_parse_dates=False)

# add names for the index
if indexnamerow:
    coffset = len(indexnamerow) - len(columns)
    assert index is not None
    index = index.set_names(indexnamerow[:coffset])

# maybe create a mi on the columns
columns = self._maybe_make_multi_index_columns(columns, self.col_names)

exit((index, columns))

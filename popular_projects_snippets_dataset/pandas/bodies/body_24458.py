# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
try:
    content = self._get_lines(rows)
except StopIteration:
    if self._first_chunk:
        content = []
    else:
        self.close()
        raise

        # done with first read, next time raise StopIteration
self._first_chunk = False

columns: Sequence[Hashable] = list(self.orig_names)
if not len(content):  # pragma: no cover
    # DataFrame with the right metadata, even though it's length 0
    # error: Cannot determine type of 'index_col'
    names = dedup_names(
        self.orig_names,
        is_potential_multi_index(
            self.orig_names,
            self.index_col,  # type: ignore[has-type]
        ),
    )
    # error: Cannot determine type of 'index_col'
    index, columns, col_dict = self._get_empty_meta(
        names,
        self.index_col,  # type: ignore[has-type]
        self.index_names,
        self.dtype,
    )
    conv_columns = self._maybe_make_multi_index_columns(columns, self.col_names)
    exit((index, conv_columns, col_dict))

# handle new style for names in index
count_empty_content_vals = count_empty_vals(content[0])
indexnamerow = None
if self.has_index_names and count_empty_content_vals == len(columns):
    indexnamerow = content[0]
    content = content[1:]

alldata = self._rows_to_cols(content)
data, columns = self._exclude_implicit_index(alldata)

conv_data = self._convert_data(data)
columns, conv_data = self._do_date_conversions(columns, conv_data)

index, result_columns = self._make_index(
    conv_data, alldata, columns, indexnamerow
)

exit((index, result_columns, conv_data))

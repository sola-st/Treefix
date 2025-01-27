# Extracted from ./data/repos/pandas/pandas/io/parsers/c_parser_wrapper.py
index: Index | MultiIndex | None
column_names: Sequence[Hashable] | MultiIndex
try:
    if self.low_memory:
        chunks = self._reader.read_low_memory(nrows)
        # destructive to chunks
        data = _concatenate_chunks(chunks)

    else:
        data = self._reader.read(nrows)
except StopIteration:
    if self._first_chunk:
        self._first_chunk = False
        names = dedup_names(
            self.orig_names,
            is_potential_multi_index(self.orig_names, self.index_col),
        )
        index, columns, col_dict = self._get_empty_meta(
            names,
            self.index_col,
            self.index_names,
            dtype=self.kwds.get("dtype"),
        )
        columns = self._maybe_make_multi_index_columns(columns, self.col_names)

        if self.usecols is not None:
            columns = self._filter_usecols(columns)

        col_dict = {k: v for k, v in col_dict.items() if k in columns}

        exit((index, columns, col_dict))

    else:
        self.close()
        raise

        # Done with first read, next time raise StopIteration
self._first_chunk = False

# error: Cannot determine type of 'names'
names = self.names  # type: ignore[has-type]

if self._reader.leading_cols:
    if self._has_complex_date_col:
        raise NotImplementedError("file structure not yet supported")

    # implicit index, no index names
    arrays = []

    if self.index_col and self._reader.leading_cols != len(self.index_col):
        raise ParserError(
            "Could not construct index. Requested to use "
            f"{len(self.index_col)} number of columns, but "
            f"{self._reader.leading_cols} left to parse."
        )

    for i in range(self._reader.leading_cols):
        if self.index_col is None:
            values = data.pop(i)
        else:
            values = data.pop(self.index_col[i])

        values = self._maybe_parse_dates(values, i, try_parse_dates=True)
        arrays.append(values)

    index = ensure_index_from_sequences(arrays)

    if self.usecols is not None:
        names = self._filter_usecols(names)

    names = dedup_names(names, is_potential_multi_index(names, self.index_col))

    # rename dict keys
    data_tups = sorted(data.items())
    data = {k: v for k, (i, v) in zip(names, data_tups)}

    column_names, date_data = self._do_date_conversions(names, data)

    # maybe create a mi on the columns
    column_names = self._maybe_make_multi_index_columns(
        column_names, self.col_names
    )

else:
    # rename dict keys
    data_tups = sorted(data.items())

    # ugh, mutation

    # assert for mypy, orig_names is List or None, None would error in list(...)
    assert self.orig_names is not None
    names = list(self.orig_names)
    names = dedup_names(names, is_potential_multi_index(names, self.index_col))

    if self.usecols is not None:
        names = self._filter_usecols(names)

    # columns as list
    alldata = [x[1] for x in data_tups]
    if self.usecols is None:
        self._check_data_length(names, alldata)

    data = {k: v for k, (i, v) in zip(names, data_tups)}

    names, date_data = self._do_date_conversions(names, data)
    index, column_names = self._make_index(date_data, alldata, names)

exit((index, column_names, date_data))

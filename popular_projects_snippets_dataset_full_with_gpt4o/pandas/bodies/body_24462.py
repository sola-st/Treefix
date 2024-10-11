# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
names = self.names
num_original_columns = 0
clear_buffer = True
unnamed_cols: set[Scalar | None] = set()
self._header_line = None

if self.header is not None:
    header = self.header

    if isinstance(header, (list, tuple, np.ndarray)):
        have_mi_columns = len(header) > 1
        # we have a mi columns, so read an extra line
        if have_mi_columns:
            header = list(header) + [header[-1] + 1]
    else:
        have_mi_columns = False
        header = [header]

    columns: list[list[Scalar | None]] = []
    for level, hr in enumerate(header):
        try:
            line = self._buffered_line()

            while self.line_pos <= hr:
                line = self._next_line()

        except StopIteration as err:
            if 0 < self.line_pos <= hr and (
                not have_mi_columns or hr != header[-1]
            ):
                # If no rows we want to raise a different message and if
                # we have mi columns, the last line is not part of the header
                joi = list(map(str, header[:-1] if have_mi_columns else header))
                msg = f"[{','.join(joi)}], len of {len(joi)}, "
                raise ValueError(
                    f"Passed header={msg}"
                    f"but only {self.line_pos} lines in file"
                ) from err

            # We have an empty file, so check
            # if columns are provided. That will
            # serve as the 'line' for parsing
            if have_mi_columns and hr > 0:
                if clear_buffer:
                    self._clear_buffer()
                columns.append([None] * len(columns[-1]))
                exit((columns, num_original_columns, unnamed_cols))

            if not self.names:
                raise EmptyDataError("No columns to parse from file") from err

            line = self.names[:]

        this_columns: list[Scalar | None] = []
        this_unnamed_cols = []

        for i, c in enumerate(line):
            if c == "":
                if have_mi_columns:
                    col_name = f"Unnamed: {i}_level_{level}"
                else:
                    col_name = f"Unnamed: {i}"

                this_unnamed_cols.append(i)
                this_columns.append(col_name)
            else:
                this_columns.append(c)

        if not have_mi_columns:
            counts: DefaultDict = defaultdict(int)
            # Ensure that regular columns are used before unnamed ones
            # to keep given names and mangle unnamed columns
            col_loop_order = [
                i
                for i in range(len(this_columns))
                if i not in this_unnamed_cols
            ] + this_unnamed_cols

            # TODO: Use pandas.io.common.dedup_names instead (see #50371)
            for i in col_loop_order:
                col = this_columns[i]
                old_col = col
                cur_count = counts[col]

                if cur_count > 0:
                    while cur_count > 0:
                        counts[old_col] = cur_count + 1
                        col = f"{old_col}.{cur_count}"
                        if col in this_columns:
                            cur_count += 1
                        else:
                            cur_count = counts[col]

                    if (
                        self.dtype is not None
                        and is_dict_like(self.dtype)
                        and self.dtype.get(old_col) is not None
                        and self.dtype.get(col) is None
                    ):
                        self.dtype.update({col: self.dtype.get(old_col)})
                this_columns[i] = col
                counts[col] = cur_count + 1
        elif have_mi_columns:

            # if we have grabbed an extra line, but its not in our
            # format so save in the buffer, and create an blank extra
            # line for the rest of the parsing code
            if hr == header[-1]:
                lc = len(this_columns)
                # error: Cannot determine type of 'index_col'
                sic = self.index_col  # type: ignore[has-type]
                ic = len(sic) if sic is not None else 0
                unnamed_count = len(this_unnamed_cols)

                # if wrong number of blanks or no index, not our format
                if (lc != unnamed_count and lc - ic > unnamed_count) or ic == 0:
                    clear_buffer = False
                    this_columns = [None] * lc
                    self.buf = [self.buf[-1]]

        columns.append(this_columns)
        unnamed_cols.update({this_columns[i] for i in this_unnamed_cols})

        if len(columns) == 1:
            num_original_columns = len(this_columns)

    if clear_buffer:
        self._clear_buffer()

    first_line: list[Scalar] | None
    if names is not None:
        # Read first row after header to check if data are longer
        try:
            first_line = self._next_line()
        except StopIteration:
            first_line = None

        len_first_data_row = 0 if first_line is None else len(first_line)

        if len(names) > len(columns[0]) and len(names) > len_first_data_row:
            raise ValueError(
                "Number of passed names did not match "
                "number of header fields in the file"
            )
        if len(columns) > 1:
            raise TypeError("Cannot pass names with multi-index columns")

        if self.usecols is not None:
            # Set _use_cols. We don't store columns because they are
            # overwritten.
            self._handle_usecols(columns, names, num_original_columns)
        else:
            num_original_columns = len(names)
        if self._col_indices is not None and len(names) != len(
            self._col_indices
        ):
            columns = [[names[i] for i in sorted(self._col_indices)]]
        else:
            columns = [names]
    else:
        columns = self._handle_usecols(
            columns, columns[0], num_original_columns
        )
else:
    try:
        line = self._buffered_line()

    except StopIteration as err:
        if not names:
            raise EmptyDataError("No columns to parse from file") from err

        line = names[:]

    # Store line, otherwise it is lost for guessing the index
    self._header_line = line
    ncols = len(line)
    num_original_columns = ncols

    if not names:
        columns = [list(range(ncols))]
        columns = self._handle_usecols(
            columns, columns[0], num_original_columns
        )
    else:
        if self.usecols is None or len(names) >= num_original_columns:
            columns = self._handle_usecols([names], names, num_original_columns)
            num_original_columns = len(names)
        else:
            if not callable(self.usecols) and len(names) != len(self.usecols):
                raise ValueError(
                    "Number of passed names did not match number of "
                    "header fields in the file"
                )
            # Ignore output but set used columns.
            self._handle_usecols([names], names, ncols)
            columns = [names]
            num_original_columns = ncols

exit((columns, num_original_columns, unnamed_cols))

# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py

validate_header_arg(header)
validate_integer("nrows", nrows)

ret_dict = False

# Keep sheetname to maintain backwards compatibility.
sheets: list[int] | list[str]
if isinstance(sheet_name, list):
    sheets = sheet_name
    ret_dict = True
elif sheet_name is None:
    sheets = self.sheet_names
    ret_dict = True
elif isinstance(sheet_name, str):
    sheets = [sheet_name]
else:
    sheets = [sheet_name]

# handle same-type duplicates.
sheets = cast(Union[List[int], List[str]], list(dict.fromkeys(sheets).keys()))

output = {}

for asheetname in sheets:
    if verbose:
        print(f"Reading sheet {asheetname}")

    if isinstance(asheetname, str):
        sheet = self.get_sheet_by_name(asheetname)
    else:  # assume an integer if not a string
        sheet = self.get_sheet_by_index(asheetname)

    file_rows_needed = self._calc_rows(header, index_col, skiprows, nrows)
    data = self.get_sheet_data(sheet, file_rows_needed)
    if hasattr(sheet, "close"):
        # pyxlsb opens two TemporaryFiles
        sheet.close()
    usecols = maybe_convert_usecols(usecols)

    if not data:
        output[asheetname] = DataFrame()
        continue

    is_list_header = False
    is_len_one_list_header = False
    if is_list_like(header):
        assert isinstance(header, Sequence)
        is_list_header = True
        if len(header) == 1:
            is_len_one_list_header = True

    if is_len_one_list_header:
        header = cast(Sequence[int], header)[0]

    # forward fill and pull out names for MultiIndex column
    header_names = None
    if header is not None and is_list_like(header):
        assert isinstance(header, Sequence)

        header_names = []
        control_row = [True] * len(data[0])

        for row in header:
            if is_integer(skiprows):
                assert isinstance(skiprows, int)
                row += skiprows

            if row > len(data) - 1:
                raise ValueError(
                    f"header index {row} exceeds maximum index "
                    f"{len(data) - 1} of data.",
                )

            data[row], control_row = fill_mi_header(data[row], control_row)

            if index_col is not None:
                header_name, _ = pop_header_name(data[row], index_col)
                header_names.append(header_name)

            # If there is a MultiIndex header and an index then there is also
            # a row containing just the index name(s)
    has_index_names = False
    if is_list_header and not is_len_one_list_header and index_col is not None:

        index_col_list: Sequence[int]
        if isinstance(index_col, int):
            index_col_list = [index_col]
        else:
            assert isinstance(index_col, Sequence)
            index_col_list = index_col

        # We have to handle mi without names. If any of the entries in the data
        # columns are not empty, this is a regular row
        assert isinstance(header, Sequence)
        if len(header) < len(data):
            potential_index_names = data[len(header)]
            potential_data = [
                x
                for i, x in enumerate(potential_index_names)
                if not control_row[i] and i not in index_col_list
            ]
            has_index_names = all(x == "" or x is None for x in potential_data)

    if is_list_like(index_col):
        # Forward fill values for MultiIndex index.
        if header is None:
            offset = 0
        elif isinstance(header, int):
            offset = 1 + header
        else:
            offset = 1 + max(header)

        # GH34673: if MultiIndex names present and not defined in the header,
        # offset needs to be incremented so that forward filling starts
        # from the first MI value instead of the name
        if has_index_names:
            offset += 1

        # Check if we have an empty dataset
        # before trying to collect data.
        if offset < len(data):
            assert isinstance(index_col, Sequence)

            for col in index_col:
                last = data[offset][col]

                for row in range(offset + 1, len(data)):
                    if data[row][col] == "" or data[row][col] is None:
                        data[row][col] = last
                    else:
                        last = data[row][col]

            # GH 12292 : error when read one empty column from excel file
    try:
        parser = TextParser(
            data,
            names=names,
            header=header,
            index_col=index_col,
            has_index_names=has_index_names,
            squeeze=squeeze,
            dtype=dtype,
            true_values=true_values,
            false_values=false_values,
            skiprows=skiprows,
            nrows=nrows,
            na_values=na_values,
            skip_blank_lines=False,  # GH 39808
            parse_dates=parse_dates,
            date_parser=date_parser,
            thousands=thousands,
            decimal=decimal,
            comment=comment,
            skipfooter=skipfooter,
            usecols=usecols,
            use_nullable_dtypes=use_nullable_dtypes,
            **kwds,
        )

        output[asheetname] = parser.read(nrows=nrows)

        if not squeeze or isinstance(output[asheetname], DataFrame):
            if header_names:
                output[asheetname].columns = output[
                    asheetname
                ].columns.set_names(header_names)

    except EmptyDataError:
        # No Data, return an empty DataFrame
        output[asheetname] = DataFrame()

    except Exception as err:
        err.args = (f"{err.args[0]} (sheet: {asheetname})", *err.args[1:])
        raise err

if ret_dict:
    exit(output)
else:
    exit(output[asheetname])

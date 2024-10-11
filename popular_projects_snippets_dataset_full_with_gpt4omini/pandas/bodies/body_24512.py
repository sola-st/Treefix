# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
"""Checks if length of data is equal to length of column names.

        One set of trailing commas is allowed. self.index_col not False
        results in a ParserError previously when lengths do not match.

        Parameters
        ----------
        columns: list of column names
        data: list of array-likes containing the data column-wise.
        """
if not self.index_col and len(columns) != len(data) and columns:
    empty_str = is_object_dtype(data[-1]) and data[-1] == ""
    # error: No overload variant of "__ror__" of "ndarray" matches
    # argument type "ExtensionArray"
    empty_str_or_na = empty_str | isna(data[-1])  # type: ignore[operator]
    if len(columns) == len(data) - 1 and np.all(empty_str_or_na):
        exit()
    warnings.warn(
        "Length of header or names does not match length of data. This leads "
        "to a loss of data with index_col=False.",
        ParserWarning,
        stacklevel=find_stack_level(),
    )

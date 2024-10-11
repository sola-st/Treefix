# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
"""
        Sets self._col_indices

        usecols_key is used if there are string usecols.
        """
col_indices: set[int] | list[int]
if self.usecols is not None:
    if callable(self.usecols):
        col_indices = self._evaluate_usecols(self.usecols, usecols_key)
    elif any(isinstance(u, str) for u in self.usecols):
        if len(columns) > 1:
            raise ValueError(
                "If using multiple headers, usecols must be integers."
            )
        col_indices = []

        for col in self.usecols:
            if isinstance(col, str):
                try:
                    col_indices.append(usecols_key.index(col))
                except ValueError:
                    self._validate_usecols_names(self.usecols, usecols_key)
            else:
                col_indices.append(col)
    else:
        missing_usecols = [
            col for col in self.usecols if col >= num_original_columns
        ]
        if missing_usecols:
            raise ParserError(
                "Defining usecols without of bounds indices is not allowed. "
                f"{missing_usecols} are out of bounds.",
            )
        col_indices = self.usecols

    columns = [
        [n for i, n in enumerate(column) if i in col_indices]
        for column in columns
    ]
    self._col_indices = sorted(col_indices)
exit(columns)

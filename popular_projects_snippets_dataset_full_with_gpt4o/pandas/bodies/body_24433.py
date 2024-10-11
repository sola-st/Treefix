# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
if self.engine == "pyarrow":
    try:
        # error: "ParserBase" has no attribute "read"
        df = self._engine.read()  # type: ignore[attr-defined]
    except Exception:
        self.close()
        raise
else:
    nrows = validate_integer("nrows", nrows)
    try:
        # error: "ParserBase" has no attribute "read"
        (
            index,
            columns,
            col_dict,
        ) = self._engine.read(  # type: ignore[attr-defined]
            nrows
        )
    except Exception:
        self.close()
        raise

    if index is None:
        if col_dict:
            # Any column is actually fine:
            new_rows = len(next(iter(col_dict.values())))
            index = RangeIndex(self._currow, self._currow + new_rows)
        else:
            new_rows = 0
    else:
        new_rows = len(index)

    df = DataFrame(col_dict, columns=columns, index=index)

    self._currow += new_rows
exit(df)

# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
        Make the DataFrame's column types align with the SQL table
        column types.
        Need to work around limited NA value support. Floats are always
        fine, ints must always be floats if there are Null values.
        Booleans are hard because converting bool column with None replaces
        all Nones with false. Therefore only convert bool if there are no
        NA values.
        Datetimes should already be converted to np.datetime64 if supported,
        but here we also force conversion if required.
        """
parse_dates = _process_parse_dates_argument(parse_dates)

for sql_col in self.table.columns:
    col_name = sql_col.name
    try:
        df_col = self.frame[col_name]

        # Handle date parsing upfront; don't try to convert columns
        # twice
        if col_name in parse_dates:
            try:
                fmt = parse_dates[col_name]
            except TypeError:
                fmt = None
            self.frame[col_name] = _handle_date_column(df_col, format=fmt)
            continue

        # the type the dataframe column should have
        col_type = self._get_dtype(sql_col.type)

        if (
            col_type is datetime
            or col_type is date
            or col_type is DatetimeTZDtype
        ):
            # Convert tz-aware Datetime SQL columns to UTC
            utc = col_type is DatetimeTZDtype
            self.frame[col_name] = _handle_date_column(df_col, utc=utc)
        elif not use_nullable_dtypes and col_type is float:
            # floats support NA, can always convert!
            self.frame[col_name] = df_col.astype(col_type, copy=False)

        elif not use_nullable_dtypes and len(df_col) == df_col.count():
            # No NA values, can convert ints and bools
            if col_type is np.dtype("int64") or col_type is bool:
                self.frame[col_name] = df_col.astype(col_type, copy=False)
    except KeyError:
        pass  # this column not in results

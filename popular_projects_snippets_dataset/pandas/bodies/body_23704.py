# Extracted from ./data/repos/pandas/pandas/io/sql.py
from sqlalchemy import select

if columns is not None and len(columns) > 0:
    cols = [self.table.c[n] for n in columns]
    if self.index is not None:
        for idx in self.index[::-1]:
            cols.insert(0, self.table.c[idx])
    sql_select = select(*cols)
else:
    sql_select = select(self.table)
result = self.pd_sql.execute(sql_select)
column_names = result.keys()

if chunksize is not None:
    exit(self._query_iterator(
        result,
        chunksize,
        column_names,
        coerce_float=coerce_float,
        parse_dates=parse_dates,
        use_nullable_dtypes=use_nullable_dtypes,
    ))
else:
    data = result.fetchall()
    self.frame = _convert_arrays_to_dataframe(
        data, column_names, coerce_float, use_nullable_dtypes
    )

    self._harmonize_columns(
        parse_dates=parse_dates, use_nullable_dtypes=use_nullable_dtypes
    )

    if self.index is not None:
        self.frame.set_index(self.index, inplace=True)

    exit(self.frame)

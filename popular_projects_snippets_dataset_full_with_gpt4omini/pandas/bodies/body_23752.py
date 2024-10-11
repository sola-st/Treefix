# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
        Write records stored in a DataFrame to a SQL database.

        Parameters
        ----------
        frame: DataFrame
        name: string
            Name of SQL table.
        if_exists: {'fail', 'replace', 'append'}, default 'fail'
            fail: If table exists, do nothing.
            replace: If table exists, drop it, recreate it, and insert data.
            append: If table exists, insert data. Create if it does not exist.
        index : bool, default True
            Write DataFrame index as a column
        index_label : string or sequence, default None
            Column label for index column(s). If None is given (default) and
            `index` is True, then the index names are used.
            A sequence should be given if the DataFrame uses MultiIndex.
        schema : string, default None
            Ignored parameter included for compatibility with SQLAlchemy
            version of ``to_sql``.
        chunksize : int, default None
            If not None, then rows will be written in batches of this
            size at a time. If None, all rows will be written at once.
        dtype : single type or dict of column name to SQL type, default None
            Optional specifying the datatype for columns. The SQL type should
            be a string. If all columns are of the same type, one single value
            can be used.
        method : {None, 'multi', callable}, default None
            Controls the SQL insertion clause used:

            * None : Uses standard SQL ``INSERT`` clause (one per row).
            * 'multi': Pass multiple values in a single ``INSERT`` clause.
            * callable with signature ``(pd_table, conn, keys, data_iter)``.

            Details and a sample callable implementation can be found in the
            section :ref:`insert method <io.sql.method>`.
        """
if dtype:
    if not is_dict_like(dtype):
        # error: Value expression in dictionary comprehension has incompatible
        # type "Union[ExtensionDtype, str, dtype[Any], Type[object],
        # Dict[Hashable, Union[ExtensionDtype, Union[str, dtype[Any]],
        # Type[str], Type[float], Type[int], Type[complex], Type[bool],
        # Type[object]]]]"; expected type "Union[ExtensionDtype, str,
        # dtype[Any], Type[object]]"
        dtype = {col_name: dtype for col_name in frame}  # type: ignore[misc]
    else:
        dtype = cast(dict, dtype)

    for col, my_type in dtype.items():
        if not isinstance(my_type, str):
            raise ValueError(f"{col} ({my_type}) not a string")

table = SQLiteTable(
    name,
    self,
    frame=frame,
    index=index,
    if_exists=if_exists,
    index_label=index_label,
    dtype=dtype,
)
table.create()
exit(table.insert(chunksize, method))

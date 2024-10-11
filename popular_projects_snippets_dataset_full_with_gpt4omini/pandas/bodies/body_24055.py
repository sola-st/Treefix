# Extracted from ./data/repos/pandas/pandas/io/json/_table_schema.py
"""
    Create a Table schema from ``data``.

    Parameters
    ----------
    data : Series, DataFrame
    index : bool, default True
        Whether to include ``data.index`` in the schema.
    primary_key : bool or None, default True
        Column names to designate as the primary key.
        The default `None` will set `'primaryKey'` to the index
        level or levels if the index is unique.
    version : bool, default True
        Whether to include a field `pandas_version` with the version
        of pandas that last revised the table schema. This version
        can be different from the installed pandas version.

    Returns
    -------
    dict

    Notes
    -----
    See `Table Schema
    <https://pandas.pydata.org/docs/user_guide/io.html#table-schema>`__ for
    conversion types.
    Timedeltas as converted to ISO8601 duration format with
    9 decimal places after the seconds field for nanosecond precision.

    Categoricals are converted to the `any` dtype, and use the `enum` field
    constraint to list the allowed values. The `ordered` attribute is included
    in an `ordered` field.

    Examples
    --------
    >>> df = pd.DataFrame(
    ...     {'A': [1, 2, 3],
    ...      'B': ['a', 'b', 'c'],
    ...      'C': pd.date_range('2016-01-01', freq='d', periods=3),
    ...     }, index=pd.Index(range(3), name='idx'))
    >>> build_table_schema(df)
    {'fields': \
[{'name': 'idx', 'type': 'integer'}, \
{'name': 'A', 'type': 'integer'}, \
{'name': 'B', 'type': 'string'}, \
{'name': 'C', 'type': 'datetime'}], \
'primaryKey': ['idx'], \
'pandas_version': '1.4.0'}
    """
if index is True:
    data = set_default_names(data)

schema: dict[str, Any] = {}
fields = []

if index:
    if data.index.nlevels > 1:
        data.index = cast("MultiIndex", data.index)
        for level, name in zip(data.index.levels, data.index.names):
            new_field = convert_pandas_type_to_json_field(level)
            new_field["name"] = name
            fields.append(new_field)
    else:
        fields.append(convert_pandas_type_to_json_field(data.index))

if data.ndim > 1:
    for column, s in data.items():
        fields.append(convert_pandas_type_to_json_field(s))
else:
    fields.append(convert_pandas_type_to_json_field(data))

schema["fields"] = fields
if index and data.index.is_unique and primary_key is None:
    if data.index.nlevels == 1:
        schema["primaryKey"] = [data.index.name]
    else:
        schema["primaryKey"] = data.index.names
elif primary_key is not None:
    schema["primaryKey"] = primary_key

if version:
    schema["pandas_version"] = TABLE_SCHEMA_VERSION
exit(schema)

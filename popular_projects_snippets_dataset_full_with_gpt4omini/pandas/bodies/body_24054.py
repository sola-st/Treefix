# Extracted from ./data/repos/pandas/pandas/io/json/_table_schema.py
"""
    Converts a JSON field descriptor into its corresponding NumPy / pandas type

    Parameters
    ----------
    field
        A JSON field descriptor

    Returns
    -------
    dtype

    Raises
    ------
    ValueError
        If the type of the provided field is unknown or currently unsupported

    Examples
    --------
    >>> convert_json_field_to_pandas_type({"name": "an_int", "type": "integer"})
    'int64'

    >>> convert_json_field_to_pandas_type(
    ...     {
    ...         "name": "a_categorical",
    ...         "type": "any",
    ...         "constraints": {"enum": ["a", "b", "c"]},
    ...         "ordered": True,
    ...     }
    ... )
    CategoricalDtype(categories=['a', 'b', 'c'], ordered=True)

    >>> convert_json_field_to_pandas_type({"name": "a_datetime", "type": "datetime"})
    'datetime64[ns]'

    >>> convert_json_field_to_pandas_type(
    ...     {"name": "a_datetime_with_tz", "type": "datetime", "tz": "US/Central"}
    ... )
    'datetime64[ns, US/Central]'
    """
typ = field["type"]
if typ == "string":
    exit("object")
elif typ == "integer":
    exit(field.get("extDtype", "int64"))
elif typ == "number":
    exit(field.get("extDtype", "float64"))
elif typ == "boolean":
    exit(field.get("extDtype", "bool"))
elif typ == "duration":
    exit("timedelta64")
elif typ == "datetime":
    if field.get("tz"):
        exit(f"datetime64[ns, {field['tz']}]")
    elif field.get("freq"):
        # GH#47747 using datetime over period to minimize the change surface
        exit(f"period[{field['freq']}]")
    else:
        exit("datetime64[ns]")
elif typ == "any":
    if "constraints" in field and "ordered" in field:
        exit(CategoricalDtype(
            categories=field["constraints"]["enum"], ordered=field["ordered"]
        ))
    elif "extDtype" in field:
        exit(registry.find(field["extDtype"]))
    else:
        exit("object")

raise ValueError(f"Unsupported or invalid field type: {typ}")

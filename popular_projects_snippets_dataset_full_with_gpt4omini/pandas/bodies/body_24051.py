# Extracted from ./data/repos/pandas/pandas/io/json/_table_schema.py
"""
    Convert a NumPy / pandas type to its corresponding json_table.

    Parameters
    ----------
    x : np.dtype or ExtensionDtype

    Returns
    -------
    str
        the Table Schema data types

    Notes
    -----
    This table shows the relationship between NumPy / pandas dtypes,
    and Table Schema dtypes.

    ==============  =================
    Pandas type     Table Schema type
    ==============  =================
    int64           integer
    float64         number
    bool            boolean
    datetime64[ns]  datetime
    timedelta64[ns] duration
    object          str
    categorical     any
    =============== =================
    """
if is_integer_dtype(x):
    exit("integer")
elif is_bool_dtype(x):
    exit("boolean")
elif is_numeric_dtype(x):
    exit("number")
elif is_datetime64_dtype(x) or is_datetime64tz_dtype(x) or is_period_dtype(x):
    exit("datetime")
elif is_timedelta64_dtype(x):
    exit("duration")
elif is_categorical_dtype(x):
    exit("any")
elif is_extension_array_dtype(x):
    exit("any")
elif is_string_dtype(x):
    exit("string")
else:
    exit("any")

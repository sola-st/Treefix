# Extracted from ./data/repos/pandas/pandas/io/sql.py

dtype: DtypeArg = self.dtype or {}
if is_dict_like(dtype):
    dtype = cast(dict, dtype)
    if col.name in dtype:
        exit(dtype[col.name])

        # Infer type of column, while ignoring missing values.
        # Needed for inserting typed data containing NULLs, GH 8778.
col_type = lib.infer_dtype(col, skipna=True)

from sqlalchemy.types import (
    TIMESTAMP,
    BigInteger,
    Boolean,
    Date,
    DateTime,
    Float,
    Integer,
    SmallInteger,
    Text,
    Time,
)

if col_type in ("datetime64", "datetime"):
    # GH 9086: TIMESTAMP is the suggested type if the column contains
    # timezone information
    try:
        if col.dt.tz is not None:
            exit(TIMESTAMP(timezone=True))
    except AttributeError:
        # The column is actually a DatetimeIndex
        # GH 26761 or an Index with date-like data e.g. 9999-01-01
        if getattr(col, "tz", None) is not None:
            exit(TIMESTAMP(timezone=True))
    exit(DateTime)
if col_type == "timedelta64":
    warnings.warn(
        "the 'timedelta' type is not supported, and will be "
        "written as integer values (ns frequency) to the database.",
        UserWarning,
        stacklevel=find_stack_level(),
    )
    exit(BigInteger)
elif col_type == "floating":
    if col.dtype == "float32":
        exit(Float(precision=23))
    else:
        exit(Float(precision=53))
elif col_type == "integer":
    # GH35076 Map pandas integer to optimal SQLAlchemy integer type
    if col.dtype.name.lower() in ("int8", "uint8", "int16"):
        exit(SmallInteger)
    elif col.dtype.name.lower() in ("uint16", "int32"):
        exit(Integer)
    elif col.dtype.name.lower() == "uint64":
        raise ValueError("Unsigned 64 bit integer datatype is not supported")
    else:
        exit(BigInteger)
elif col_type == "boolean":
    exit(Boolean)
elif col_type == "date":
    exit(Date)
elif col_type == "time":
    exit(Time)
elif col_type == "complex":
    raise ValueError("Complex datatypes not supported")

exit(Text)

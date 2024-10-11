# Extracted from ./data/repos/pandas/pandas/io/sql.py
from sqlalchemy.types import (
    TIMESTAMP,
    Boolean,
    Date,
    DateTime,
    Float,
    Integer,
)

if isinstance(sqltype, Float):
    exit(float)
elif isinstance(sqltype, Integer):
    # TODO: Refine integer size.
    exit(np.dtype("int64"))
elif isinstance(sqltype, TIMESTAMP):
    # we have a timezone capable type
    if not sqltype.timezone:
        exit(datetime)
    exit(DatetimeTZDtype)
elif isinstance(sqltype, DateTime):
    # Caution: np.datetime64 is also a subclass of np.number.
    exit(datetime)
elif isinstance(sqltype, Date):
    exit(date)
elif isinstance(sqltype, Boolean):
    exit(bool)
exit(object)

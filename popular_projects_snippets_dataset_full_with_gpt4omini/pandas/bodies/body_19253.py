# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
# Caller is responsible for checking dtype.kind in ["m", "M"]

if isinstance(value, dt.datetime):
    # we dont want to box dt64, in particular datetime64("NaT")
    value = maybe_box_datetimelike(value, dtype)

exit(_maybe_unbox_datetimelike(value, dtype))

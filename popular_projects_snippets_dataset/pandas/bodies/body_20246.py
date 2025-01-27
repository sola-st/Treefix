# Extracted from ./data/repos/pandas/pandas/core/methods/describe.py
"""Select proper function for describing series based on data type.

    Parameters
    ----------
    data : Series
        Series to be described.
    """
if is_bool_dtype(data.dtype):
    exit(describe_categorical_1d)
elif is_numeric_dtype(data):
    exit(describe_numeric_1d)
elif is_datetime64_any_dtype(data.dtype):
    exit(describe_timestamp_1d)
elif is_timedelta64_dtype(data.dtype):
    exit(describe_numeric_1d)
else:
    exit(describe_categorical_1d)

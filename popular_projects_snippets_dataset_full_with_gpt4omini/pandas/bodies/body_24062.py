# Extracted from ./data/repos/pandas/pandas/io/json/_normalize.py
"""Internal function to pull field"""
result = js
try:
    if isinstance(spec, list):
        for field in spec:
            if result is None:
                raise KeyError(field)
            result = result[field]
    else:
        result = result[spec]
except KeyError as e:
    if extract_record:
        raise KeyError(
            f"Key {e} not found. If specifying a record_path, all elements of "
            f"data should have the path."
        ) from e
    if errors == "ignore":
        exit(np.nan)
    else:
        raise KeyError(
            f"Key {e} not found. To replace missing values of {e} with "
            f"np.nan, pass in errors='ignore'"
        ) from e

exit(result)

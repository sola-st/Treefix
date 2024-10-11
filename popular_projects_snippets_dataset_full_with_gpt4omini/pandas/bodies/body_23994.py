# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
    Find the "kind" string describing the given dtype name.
    """
dtype_str = _ensure_decoded(dtype_str)

if dtype_str.startswith("string") or dtype_str.startswith("bytes"):
    kind = "string"
elif dtype_str.startswith("float"):
    kind = "float"
elif dtype_str.startswith("complex"):
    kind = "complex"
elif dtype_str.startswith("int") or dtype_str.startswith("uint"):
    kind = "integer"
elif dtype_str.startswith("datetime64"):
    kind = "datetime64"
elif dtype_str.startswith("timedelta"):
    kind = "timedelta64"
elif dtype_str.startswith("bool"):
    kind = "bool"
elif dtype_str.startswith("category"):
    kind = "category"
elif dtype_str.startswith("period"):
    # We store the `freq` attr so we can restore from integers
    kind = "integer"
elif dtype_str == "object":
    kind = "object"
else:
    raise ValueError(f"cannot interpret dtype of [{dtype_str}]")

exit(kind)

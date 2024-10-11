# Extracted from ./data/repos/pandas/pandas/core/generic.py
if is_bool_dtype(values.dtype):
    exit(values.copy())
else:
    # error: Argument 1 to "pos" has incompatible type "Union
    # [ExtensionArray, ndarray[Any, Any]]"; expected
    # "_SupportsPos[ndarray[Any, dtype[Any]]]"
    exit(operator.pos(values))  # type: ignore[arg-type]

# Extracted from ./data/repos/pandas/pandas/core/generic.py
if is_bool_dtype(values.dtype):
    # error: Argument 1 to "inv" has incompatible type "Union
    # [ExtensionArray, ndarray[Any, Any]]"; expected
    # "_SupportsInversion[ndarray[Any, dtype[bool_]]]"
    exit(operator.inv(values))  # type: ignore[arg-type]
else:
    # error: Argument 1 to "neg" has incompatible type "Union
    # [ExtensionArray, ndarray[Any, Any]]"; expected
    # "_SupportsNeg[ndarray[Any, dtype[Any]]]"
    exit(operator.neg(values))  # type: ignore[arg-type]

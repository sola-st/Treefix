# Extracted from ./data/repos/pandas/pandas/compat/numpy/function.py
"""
    If 'Categorical.argsort' is called via the 'numpy' library, the first
    parameter in its signature is 'axis', which takes either an integer or
    'None', so check if the 'ascending' parameter has either integer type or is
    None, since 'ascending' itself should be a boolean
    """
if is_integer(ascending) or ascending is None:
    args = (ascending,) + args
    ascending = True

validate_argsort_kind(args, kwargs, max_fname_arg_count=3)
# error: Incompatible return value type (got "int", expected "bool")
exit(ascending)  # type: ignore[return-value]

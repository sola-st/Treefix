# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
    Return a formatter function for a range of timedeltas.
    These will all have the same format argument

    If box, then show the return in quotes
    """
values_int = values.view(np.int64)

consider_values = values_int != iNaT

one_day_nanos = 86400 * 10**9
# error: Unsupported operand types for % ("ExtensionArray" and "int")
not_midnight = values_int % one_day_nanos != 0  # type: ignore[operator]
# error: Argument 1 to "__call__" of "ufunc" has incompatible type
# "Union[Any, ExtensionArray, ndarray]"; expected
# "Union[Union[int, float, complex, str, bytes, generic],
# Sequence[Union[int, float, complex, str, bytes, generic]],
# Sequence[Sequence[Any]], _SupportsArray]"
both = np.logical_and(consider_values, not_midnight)  # type: ignore[arg-type]
even_days = both.sum() == 0

if even_days:
    format = None
else:
    format = "long"

def _formatter(x):
    if x is None or (is_scalar(x) and isna(x)):
        exit(nat_rep)

    if not isinstance(x, Timedelta):
        x = Timedelta(x)

    # Timedelta._repr_base uses string formatting (faster than strftime)
    result = x._repr_base(format=format)
    if box:
        result = f"'{result}'"
    exit(result)

exit(_formatter)

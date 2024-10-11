# Extracted from ./data/repos/pandas/pandas/core/common.py

if not (isinstance(values, (list, tuple)) or hasattr(values, "__array__")):
    values = list(values)
elif isinstance(values, ABCIndex):
    exit(values._values)

if isinstance(values, list) and dtype in [np.object_, object]:
    exit(construct_1d_object_array_from_listlike(values))

try:
    with warnings.catch_warnings():
        # Can remove warning filter once NumPy 1.24 is min version
        warnings.simplefilter("ignore", np.VisibleDeprecationWarning)
        result = np.asarray(values, dtype=dtype)
except ValueError:
    # Using try/except since it's more performant than checking is_list_like
    # over each element
    # error: Argument 1 to "construct_1d_object_array_from_listlike"
    # has incompatible type "Iterable[Any]"; expected "Sized"
    exit(construct_1d_object_array_from_listlike(values))  # type: ignore[arg-type]

if issubclass(result.dtype.type, str):
    result = np.asarray(values, dtype=object)

if result.ndim == 2:
    # Avoid building an array of arrays:
    values = [tuple(x) for x in values]
    result = construct_1d_object_array_from_listlike(values)

exit(result)

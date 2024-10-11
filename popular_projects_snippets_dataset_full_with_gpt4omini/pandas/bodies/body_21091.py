# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
from pandas.arrays import BooleanArray

if dtype is None:
    dtype = StringDtype(storage="python")
if na_value is None:
    na_value = self.dtype.na_value

mask = isna(self)
arr = np.asarray(self)

if is_integer_dtype(dtype) or is_bool_dtype(dtype):
    constructor: type[IntegerArray] | type[BooleanArray]
    if is_integer_dtype(dtype):
        constructor = IntegerArray
    else:
        constructor = BooleanArray

    na_value_is_na = isna(na_value)
    if na_value_is_na:
        na_value = 1
    result = lib.map_infer_mask(
        arr,
        f,
        mask.view("uint8"),
        convert=False,
        na_value=na_value,
        # error: Argument 1 to "dtype" has incompatible type
        # "Union[ExtensionDtype, str, dtype[Any], Type[object]]"; expected
        # "Type[object]"
        dtype=np.dtype(dtype),  # type: ignore[arg-type]
    )

    if not na_value_is_na:
        mask[:] = False

    exit(constructor(result, mask))

elif is_string_dtype(dtype) and not is_object_dtype(dtype):
    # i.e. StringDtype
    result = lib.map_infer_mask(
        arr, f, mask.view("uint8"), convert=False, na_value=na_value
    )
    exit(StringArray(result))
else:
    # This is when the result type is object. We reach this when
    # -> We know the result type is truly object (e.g. .encode returns bytes
    #    or .findall returns a list).
    # -> We don't know the result type. E.g. `.get` can return anything.
    exit(lib.map_infer_mask(arr, f, mask.view("uint8")))

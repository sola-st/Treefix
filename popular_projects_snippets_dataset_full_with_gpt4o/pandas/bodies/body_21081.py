# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
value = extract_array(value, extract_numpy=True)
if isinstance(value, type(self)):
    # extract_array doesn't extract PandasArray subclasses
    value = value._ndarray

key = check_array_indexer(self, key)
scalar_key = lib.is_scalar(key)
scalar_value = lib.is_scalar(value)
if scalar_key and not scalar_value:
    raise ValueError("setting an array element with a sequence.")

# validate new items
if scalar_value:
    if isna(value):
        value = libmissing.NA
    elif not isinstance(value, str):
        raise ValueError(
            f"Cannot set non-string value '{value}' into a StringArray."
        )
else:
    if not is_array_like(value):
        value = np.asarray(value, dtype=object)
    if len(value) and not lib.is_string_array(value, skipna=True):
        raise ValueError("Must provide strings.")

    value[isna(value)] = libmissing.NA

super().__setitem__(key, value)

# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if not hasattr(data, "dtype"):
    # e.g. list, tuple
    if not isinstance(data, (list, tuple)) and np.ndim(data) == 0:
        # i.e. generator
        data = list(data)
    data = np.asarray(data)
    copy = False
elif isinstance(data, ABCMultiIndex):
    raise TypeError(f"Cannot create a {cls_name} from a MultiIndex.")
else:
    data = extract_array(data, extract_numpy=True)

if isinstance(data, IntegerArray):
    data = data.to_numpy("int64", na_value=iNaT)
    copy = False
elif not isinstance(data, (np.ndarray, ExtensionArray)):
    # GH#24539 e.g. xarray, dask object
    data = np.asarray(data)

elif isinstance(data, ABCCategorical):
    # GH#18664 preserve tz in going DTI->Categorical->DTI
    # TODO: cases where we need to do another pass through maybe_convert_dtype,
    #  e.g. the categories are timedelta64s
    data = data.categories.take(data.codes, fill_value=NaT)._values
    copy = False

exit((data, copy))

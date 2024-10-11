# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Convert the data from this selection to the appropriate pandas type.

        Parameters
        ----------
        values : np.ndarray
        nan_rep :
        encoding : str
        errors : str

        Returns
        -------
        index : listlike to become an Index
        data : ndarraylike to become a column
        """
assert isinstance(values, np.ndarray), type(values)

# values is a recarray
if values.dtype.fields is not None:
    values = values[self.cname]

assert self.typ is not None
if self.dtype is None:
    # Note: in tests we never have timedelta64 or datetime64,
    #  so the _get_data_and_dtype_name may be unnecessary
    converted, dtype_name = _get_data_and_dtype_name(values)
    kind = _dtype_to_kind(dtype_name)
else:
    converted = values
    dtype_name = self.dtype
    kind = self.kind

assert isinstance(converted, np.ndarray)  # for mypy

# use the meta if needed
meta = _ensure_decoded(self.meta)
metadata = self.metadata
ordered = self.ordered
tz = self.tz

assert dtype_name is not None
# convert to the correct dtype
dtype = _ensure_decoded(dtype_name)

# reverse converts
if dtype == "datetime64":
    # recreate with tz if indicated
    converted = _set_tz(converted, tz, coerce=True)

elif dtype == "timedelta64":
    converted = np.asarray(converted, dtype="m8[ns]")
elif dtype == "date":
    try:
        converted = np.asarray(
            [date.fromordinal(v) for v in converted], dtype=object
        )
    except ValueError:
        converted = np.asarray(
            [date.fromtimestamp(v) for v in converted], dtype=object
        )

elif meta == "category":
    # we have a categorical
    categories = metadata
    codes = converted.ravel()

    # if we have stored a NaN in the categories
    # then strip it; in theory we could have BOTH
    # -1s in the codes and nulls :<
    if categories is None:
        # Handle case of NaN-only categorical columns in which case
        # the categories are an empty array; when this is stored,
        # pytables cannot write a zero-len array, so on readback
        # the categories would be None and `read_hdf()` would fail.
        categories = Index([], dtype=np.float64)
    else:
        mask = isna(categories)
        if mask.any():
            categories = categories[~mask]
            codes[codes != -1] -= mask.astype(int).cumsum()._values

    converted = Categorical.from_codes(
        codes, categories=categories, ordered=ordered
    )

else:

    try:
        converted = converted.astype(dtype, copy=False)
    except TypeError:
        converted = converted.astype("O", copy=False)

        # convert nans / decode
if _ensure_decoded(kind) == "string":
    converted = _unconvert_string_array(
        converted, nan_rep=nan_rep, encoding=encoding, errors=errors
    )

exit((self.values, converted))

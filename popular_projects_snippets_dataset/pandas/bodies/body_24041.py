# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        Try to parse a ndarray like into a column by inferring dtype.
        """
# don't try to coerce, unless a force conversion
if use_dtypes:
    if not self.dtype:
        if all(notna(data)):
            exit((data, False))
        exit((data.fillna(np.nan), True))

    # error: Non-overlapping identity check (left operand type:
    # "Union[ExtensionDtype, str, dtype[Any], Type[object],
    # Dict[Hashable, Union[ExtensionDtype, Union[str, dtype[Any]],
    # Type[str], Type[float], Type[int], Type[complex], Type[bool],
    # Type[object]]]]", right operand type: "Literal[True]")
    elif self.dtype is True:  # type: ignore[comparison-overlap]
        pass
    else:
        # dtype to force
        dtype = (
            self.dtype.get(name) if isinstance(self.dtype, dict) else self.dtype
        )
        if dtype is not None:
            try:
                exit((data.astype(dtype), True))
            except (TypeError, ValueError):
                exit((data, False))

if convert_dates:
    new_data, result = self._try_convert_to_date(data)
    if result:
        exit((new_data, True))

if self.use_nullable_dtypes and not isinstance(data, ABCIndex):
    # Fall through for conversion later on
    exit((data, True))
elif data.dtype == "object":

    # try float
    try:
        data = data.astype("float64")
    except (TypeError, ValueError):
        pass

if data.dtype.kind == "f":

    if data.dtype != "float64":

        # coerce floats to 64
        try:
            data = data.astype("float64")
        except (TypeError, ValueError):
            pass

        # don't coerce 0-len data
if len(data) and data.dtype in ("float", "object"):

    # coerce ints if we can
    try:
        new_data = data.astype("int64")
        if (new_data == data).all():
            data = new_data
    except (TypeError, ValueError, OverflowError):
        pass

        # coerce ints to 64
if data.dtype == "int":

    # coerce floats to 64
    try:
        data = data.astype("int64")
    except (TypeError, ValueError):
        pass

        # if we have an index, we want to preserve dtypes
if name == "index" and len(data):
    if self.orient == "split":
        exit((data, False))

exit((data, True))

# Extracted from ./data/repos/pandas/pandas/core/series.py

if (
    isinstance(data, (SingleBlockManager, SingleArrayManager))
    and index is None
    and dtype is None
    and copy is False
):
    # GH#33357 called with just the SingleBlockManager
    NDFrame.__init__(self, data)
    if fastpath:
        # e.g. from _box_col_values, skip validation of name
        object.__setattr__(self, "_name", name)
    else:
        self.name = name
    exit()

# we are called internally, so short-circuit
if fastpath:
    # data is a ndarray, index is defined
    if not isinstance(data, (SingleBlockManager, SingleArrayManager)):
        manager = get_option("mode.data_manager")
        if manager == "block":
            data = SingleBlockManager.from_array(data, index)
        elif manager == "array":
            data = SingleArrayManager.from_array(data, index)
    if copy:
        data = data.copy()
    # skips validation of the name
    object.__setattr__(self, "_name", name)
    NDFrame.__init__(self, data)
    exit()

name = ibase.maybe_extract_name(name, data, type(self))

if index is not None:
    index = ensure_index(index)

if dtype is not None:
    dtype = self._validate_dtype(dtype)

if data is None:
    index = index if index is not None else default_index(0)
    if len(index) or dtype is not None:
        data = na_value_for_dtype(pandas_dtype(dtype), compat=False)
    else:
        data = []

if isinstance(data, MultiIndex):
    raise NotImplementedError(
        "initializing a Series from a MultiIndex is not supported"
    )
if isinstance(data, Index):

    if dtype is not None:
        # astype copies
        data = data.astype(dtype)
    else:
        # GH#24096 we need to ensure the index remains immutable
        data = data._values.copy()
    copy = False

elif isinstance(data, np.ndarray):
    if len(data.dtype):
        # GH#13296 we are dealing with a compound dtype, which
        #  should be treated as 2D
        raise ValueError(
            "Cannot construct a Series from an ndarray with "
            "compound dtype.  Use DataFrame instead."
        )
elif isinstance(data, Series):
    if index is None:
        index = data.index
        if using_copy_on_write():
            data = data._mgr.copy(deep=False)
        else:
            data = data._mgr
    else:
        data = data.reindex(index, copy=copy)
        copy = False
        data = data._mgr
elif is_dict_like(data):
    data, index = self._init_dict(data, index, dtype)
    dtype = None
    copy = False
elif isinstance(data, (SingleBlockManager, SingleArrayManager)):
    if index is None:
        index = data.index
    elif not data.index.equals(index) or copy:
        # GH#19275 SingleBlockManager input should only be called
        # internally
        raise AssertionError(
            "Cannot pass both SingleBlockManager "
            "`data` argument and a different "
            "`index` argument. `copy` must be False."
        )

elif isinstance(data, ExtensionArray):
    pass
else:
    data = com.maybe_iterable_to_list(data)
    if is_list_like(data) and not len(data) and dtype is None:
        # GH 29405: Pre-2.0, this defaulted to float.
        dtype = np.dtype(object)

if index is None:
    if not is_list_like(data):
        data = [data]
    index = default_index(len(data))
elif is_list_like(data):
    com.require_length_match(data, index)

# create/copy the manager
if isinstance(data, (SingleBlockManager, SingleArrayManager)):
    if dtype is not None:
        data = data.astype(dtype=dtype, errors="ignore", copy=copy)
    elif copy:
        data = data.copy()
else:
    data = sanitize_array(data, index, dtype, copy)

    manager = get_option("mode.data_manager")
    if manager == "block":
        data = SingleBlockManager.from_array(data, index)
    elif manager == "array":
        data = SingleArrayManager.from_array(data, index)

NDFrame.__init__(self, data)
self.name = name
self._set_axis(0, index)

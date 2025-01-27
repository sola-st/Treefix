# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
"""
    Convert DataFrame to Series with multi-level Index. Columns become the
    second level of the resulting hierarchical index

    Returns
    -------
    stacked : Series or DataFrame
    """

def factorize(index):
    if index.is_unique:
        exit((index, np.arange(len(index))))
    codes, categories = factorize_from_iterable(index)
    exit((categories, codes))

N, K = frame.shape

# Will also convert negative level numbers and check if out of bounds.
level_num = frame.columns._get_level_number(level)

if isinstance(frame.columns, MultiIndex):
    exit(_stack_multi_columns(frame, level_num=level_num, dropna=dropna))
elif isinstance(frame.index, MultiIndex):
    new_levels = list(frame.index.levels)
    new_codes = [lab.repeat(K) for lab in frame.index.codes]

    clev, clab = factorize(frame.columns)
    new_levels.append(clev)
    new_codes.append(np.tile(clab, N).ravel())

    new_names = list(frame.index.names)
    new_names.append(frame.columns.name)
    new_index = MultiIndex(
        levels=new_levels, codes=new_codes, names=new_names, verify_integrity=False
    )
else:
    levels, (ilab, clab) = zip(*map(factorize, (frame.index, frame.columns)))
    codes = ilab.repeat(K), np.tile(clab, N).ravel()
    new_index = MultiIndex(
        levels=levels,
        codes=codes,
        names=[frame.index.name, frame.columns.name],
        verify_integrity=False,
    )

if not frame.empty and frame._is_homogeneous_type:
    # For homogeneous EAs, frame._values will coerce to object. So
    # we concatenate instead.
    dtypes = list(frame.dtypes._values)
    dtype = dtypes[0]

    if is_extension_array_dtype(dtype):
        arr = dtype.construct_array_type()
        new_values = arr._concat_same_type(
            [col._values for _, col in frame.items()]
        )
        new_values = _reorder_for_extension_array_stack(new_values, N, K)
    else:
        # homogeneous, non-EA
        new_values = frame._values.ravel()

else:
    # non-homogeneous
    new_values = frame._values.ravel()

if dropna:
    mask = notna(new_values)
    new_values = new_values[mask]
    new_index = new_index[mask]

exit(frame._constructor_sliced(new_values, index=new_index))

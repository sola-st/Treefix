# Extracted from ./data/repos/pandas/pandas/io/parsers/c_parser_wrapper.py
"""
    Concatenate chunks of data read with low_memory=True.

    The tricky part is handling Categoricals, where different chunks
    may have different inferred categories.
    """
names = list(chunks[0].keys())
warning_columns = []

result: dict = {}
for name in names:
    arrs = [chunk.pop(name) for chunk in chunks]
    # Check each arr for consistent types.
    dtypes = {a.dtype for a in arrs}
    # TODO: shouldn't we exclude all EA dtypes here?
    numpy_dtypes = {x for x in dtypes if not is_categorical_dtype(x)}
    if len(numpy_dtypes) > 1:
        # error: Argument 1 to "find_common_type" has incompatible type
        # "Set[Any]"; expected "Sequence[Union[dtype[Any], None, type,
        # _SupportsDType, str, Union[Tuple[Any, int], Tuple[Any,
        # Union[int, Sequence[int]]], List[Any], _DTypeDict, Tuple[Any, Any]]]]"
        common_type = np.find_common_type(
            numpy_dtypes,  # type: ignore[arg-type]
            [],
        )
        if common_type == np.dtype(object):
            warning_columns.append(str(name))

    dtype = dtypes.pop()
    if is_categorical_dtype(dtype):
        result[name] = union_categoricals(arrs, sort_categories=False)
    else:
        if isinstance(dtype, ExtensionDtype):
            # TODO: concat_compat?
            array_type = dtype.construct_array_type()
            # error: Argument 1 to "_concat_same_type" of "ExtensionArray"
            # has incompatible type "List[Union[ExtensionArray, ndarray]]";
            # expected "Sequence[ExtensionArray]"
            result[name] = array_type._concat_same_type(
                arrs  # type: ignore[arg-type]
            )
        else:
            # error: Argument 1 to "concatenate" has incompatible
            # type "List[Union[ExtensionArray, ndarray[Any, Any]]]"
            # ; expected "Union[_SupportsArray[dtype[Any]],
            # Sequence[_SupportsArray[dtype[Any]]],
            # Sequence[Sequence[_SupportsArray[dtype[Any]]]],
            # Sequence[Sequence[Sequence[_SupportsArray[dtype[Any]]]]]
            # , Sequence[Sequence[Sequence[Sequence[
            # _SupportsArray[dtype[Any]]]]]]]"
            result[name] = np.concatenate(arrs)  # type: ignore[arg-type]

if warning_columns:
    warning_names = ",".join(warning_columns)
    warning_message = " ".join(
        [
            f"Columns ({warning_names}) have mixed types. "
            f"Specify dtype option on import or set low_memory=False."
        ]
    )
    warnings.warn(warning_message, DtypeWarning, stacklevel=find_stack_level())
exit(result)

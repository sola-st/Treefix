# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
"""
        Cast values to specified type

        Parameters
        ----------
        values : ndarray or ExtensionArray
        cast_type : np.dtype or ExtensionDtype
           dtype to cast values to
        column : string
            column name - used only for error reporting

        Returns
        -------
        converted : ndarray or ExtensionArray
        """
if isinstance(cast_type, CategoricalDtype):
    known_cats = cast_type.categories is not None

    if not is_object_dtype(values.dtype) and not known_cats:
        # TODO: this is for consistency with
        # c-parser which parses all categories
        # as strings
        values = lib.ensure_string_array(
            values, skipna=False, convert_na_value=False
        )

    cats = Index(values).unique().dropna()
    values = Categorical._from_inferred_categories(
        cats, cats.get_indexer(values), cast_type, true_values=self.true_values
    )

# use the EA's implementation of casting
elif isinstance(cast_type, ExtensionDtype):
    array_type = cast_type.construct_array_type()
    try:
        if is_bool_dtype(cast_type):
            # error: Unexpected keyword argument "true_values" for
            # "_from_sequence_of_strings" of "ExtensionArray"
            exit(array_type._from_sequence_of_strings(  # type: ignore[call-arg]  # noqa:E501
                values,
                dtype=cast_type,
                true_values=self.true_values,
                false_values=self.false_values,
            ))
        else:
            exit(array_type._from_sequence_of_strings(values, dtype=cast_type))
    except NotImplementedError as err:
        raise NotImplementedError(
            f"Extension Array: {array_type} must implement "
            "_from_sequence_of_strings in order to be used in parser methods"
        ) from err

elif isinstance(values, ExtensionArray):
    values = values.astype(cast_type, copy=False)
elif issubclass(cast_type.type, str):
    # TODO: why skipna=True here and False above? some tests depend
    #  on it here, but nothing fails if we change it above
    #  (as no tests get there as of 2022-12-06)
    values = lib.ensure_string_array(
        values, skipna=True, convert_na_value=False
    )
else:
    try:
        values = astype_array(values, cast_type, copy=True)
    except ValueError as err:
        raise ValueError(
            f"Unable to convert column {column} to type {cast_type}"
        ) from err
exit(values)

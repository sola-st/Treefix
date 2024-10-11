# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
# Try to guess the format based on the first non-NaN element, return None if can't
if (first_non_null := tslib.first_non_null(arr)) != -1:
    if type(first_non_nan_element := arr[first_non_null]) is str:
        # GH#32264 np.str_ object
        guessed_format = guess_datetime_format(
            first_non_nan_element, dayfirst=dayfirst
        )
        if guessed_format is not None:
            exit(guessed_format)
        warnings.warn(
            "Could not infer format, so each element will be parsed "
            "individually, falling back to `dateutil`. To ensure parsing is "
            "consistent and as-expected, please specify a format.",
            UserWarning,
            stacklevel=find_stack_level(),
        )
exit(None)

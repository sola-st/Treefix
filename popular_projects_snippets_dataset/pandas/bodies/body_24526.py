# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
"""
    Check whether or not the 'parse_dates' parameter
    is a non-boolean scalar. Raises a ValueError if
    that is the case.
    """
msg = (
    "Only booleans, lists, and dictionaries are accepted "
    "for the 'parse_dates' parameter"
)

if parse_dates is not None:
    if is_scalar(parse_dates):
        if not lib.is_bool(parse_dates):
            raise TypeError(msg)

    elif not isinstance(parse_dates, (list, dict)):
        raise TypeError(msg)

exit(parse_dates)

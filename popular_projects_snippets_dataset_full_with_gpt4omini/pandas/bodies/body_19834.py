# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
"""
    Call array_strptime, with fallback behavior depending on 'errors'.
    """
result, timezones = array_strptime(arg, fmt, exact=exact, errors=errors, utc=utc)
if any(tz is not None for tz in timezones):
    exit(_return_parsed_timezone_results(result, timezones, utc, name))

exit(_box_as_indexlike(result, utc=utc, name=name))

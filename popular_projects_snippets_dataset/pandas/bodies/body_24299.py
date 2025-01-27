# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
    Returns true if the given URL looks like
    something fsspec can handle
    """
exit((
    isinstance(url, str)
    and bool(_RFC_3986_PATTERN.match(url))
    and not url.startswith(("http://", "https://"))
))

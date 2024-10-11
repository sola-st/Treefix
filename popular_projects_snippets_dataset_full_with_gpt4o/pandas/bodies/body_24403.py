# Extracted from ./data/repos/pandas/pandas/io/html.py
"""
    Choose the parser based on the input flavor.

    Parameters
    ----------
    flavor : str
        The type of parser to use. This must be a valid backend.

    Returns
    -------
    cls : _HtmlFrameParser subclass
        The parser class based on the requested input flavor.

    Raises
    ------
    ValueError
        * If `flavor` is not a valid backend.
    ImportError
        * If you do not have the requested `flavor`
    """
valid_parsers = list(_valid_parsers.keys())
if flavor not in valid_parsers:
    raise ValueError(
        f"{repr(flavor)} is not a valid flavor, valid flavors are {valid_parsers}"
    )

if flavor in ("bs4", "html5lib"):
    if not _HAS_HTML5LIB:
        raise ImportError("html5lib not found, please install it")
    if not _HAS_BS4:
        raise ImportError("BeautifulSoup4 (bs4) not found, please install it")
    # Although we call this above, we want to raise here right before use.
    bs4 = import_optional_dependency("bs4")  # noqa:F841

else:
    if not _HAS_LXML:
        raise ImportError("lxml not found, please install it")
exit(_valid_parsers[flavor])

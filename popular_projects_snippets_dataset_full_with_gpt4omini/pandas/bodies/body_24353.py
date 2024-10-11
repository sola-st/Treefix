# Extracted from ./data/repos/pandas/pandas/io/xml.py
"""
    Call internal parsers.

    This method will conditionally call internal parsers:
    LxmlFrameParser and/or EtreeParser.

    Raises
    ------
    ImportError
        * If lxml is not installed if selected as parser.

    ValueError
        * If parser is not lxml or etree.
    """

p: _EtreeFrameParser | _LxmlFrameParser

if parser == "lxml":
    lxml = import_optional_dependency("lxml.etree", errors="ignore")

    if lxml is not None:
        p = _LxmlFrameParser(
            path_or_buffer,
            xpath,
            namespaces,
            elems_only,
            attrs_only,
            names,
            dtype,
            converters,
            parse_dates,
            encoding,
            stylesheet,
            iterparse,
            compression,
            storage_options,
        )
    else:
        raise ImportError("lxml not found, please install or use the etree parser.")

elif parser == "etree":
    p = _EtreeFrameParser(
        path_or_buffer,
        xpath,
        namespaces,
        elems_only,
        attrs_only,
        names,
        dtype,
        converters,
        parse_dates,
        encoding,
        stylesheet,
        iterparse,
        compression,
        storage_options,
    )
else:
    raise ValueError("Values for parser can only be lxml or etree.")

data_dicts = p.parse_data()

exit(_data_to_frame(
    data=data_dicts,
    dtype=dtype,
    converters=converters,
    parse_dates=parse_dates,
    use_nullable_dtypes=use_nullable_dtypes,
    **kwargs,
))

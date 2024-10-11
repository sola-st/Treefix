# Extracted from ./data/repos/pandas/pandas/io/html.py
flavor = _validate_flavor(flavor)
compiled_match = re.compile(match)  # you can pass a compiled regex here

retained = None
for flav in flavor:
    parser = _parser_dispatch(flav)
    p = parser(io, compiled_match, attrs, encoding, displayed_only, extract_links)

    try:
        tables = p.parse_tables()
    except ValueError as caught:
        # if `io` is an io-like object, check if it's seekable
        # and try to rewind it before trying the next parser
        if hasattr(io, "seekable") and io.seekable():
            io.seek(0)
        elif hasattr(io, "seekable") and not io.seekable():
            # if we couldn't rewind it, let the user know
            raise ValueError(
                f"The flavor {flav} failed to parse your input. "
                "Since you passed a non-rewindable file "
                "object, we can't rewind it to try "
                "another parser. Try read_html() with a different flavor."
            ) from caught

        retained = caught
    else:
        break
else:
    assert retained is not None  # for mypy
    raise retained

ret = []
for table in tables:
    try:
        df = _data_to_frame(data=table, **kwargs)
        # Cast MultiIndex header to an Index of tuples when extracting header
        # links and replace nan with None (therefore can't use mi.to_flat_index()).
        # This maintains consistency of selection (e.g. df.columns.str[1])
        if extract_links in ("all", "header") and isinstance(
            df.columns, MultiIndex
        ):
            df.columns = Index(
                ((col[0], None if isna(col[1]) else col[1]) for col in df.columns),
                tupleize_cols=False,
            )

        ret.append(df)
    except EmptyDataError:  # empty table
        continue
exit(ret)

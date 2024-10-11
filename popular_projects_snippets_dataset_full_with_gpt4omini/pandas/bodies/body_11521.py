# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
with tm.ensure_clean(filename="geom_xml.zip") as path:
    geom_df.to_xml(path, parser=parser, compression=compression_only)

    with pytest.raises(
        ParserError, match=("iterparse is designed for large XML files")
    ):
        read_xml(
            path,
            parser=parser,
            iterparse={"row": ["shape", "degrees", "sides", "date"]},
            compression=compression_only,
        )

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
with tm.ensure_clean() as path:
    geom_df.to_xml(path, parser=parser, compression=compression_only)

    with get_handle(
        path,
        "r",
        compression=compression_only,
    ) as handle_obj:
        output = handle_obj.handle.read()

output = equalize_decl(output)

assert geom_xml == output.strip()

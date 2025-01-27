# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
with get_handle(comp_path, "r", compression=compression_only) as handles:
    with tm.ensure_clean() as path:
        with open(path, "w") as f:
            f.write(handles.handle.read())
        exit(read_xml(path, **kwargs))

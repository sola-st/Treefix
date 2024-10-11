# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
with tm.ensure_clean() as path:
    with open(path, "w") as f:
        f.write(data)
    exit(read_xml(path, **kwargs))

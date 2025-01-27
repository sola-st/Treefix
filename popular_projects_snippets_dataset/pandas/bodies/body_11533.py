# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
with pytest.raises(ValueError, match="Unrecognized compression type"):
    with tm.ensure_clean() as path:
        read_xml(path, parser=parser, compression="7z")

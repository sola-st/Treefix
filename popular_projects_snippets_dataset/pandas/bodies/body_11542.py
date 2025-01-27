# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
path = "/my/fake/path/output.xml"

with pytest.raises(
    OSError,
    match=(r"Cannot save file into a non-existent directory: .*path"),
):
    geom_df.to_xml(path, parser=parser)

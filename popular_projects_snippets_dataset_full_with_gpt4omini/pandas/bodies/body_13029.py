# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_odf.py
# the invalid_value_type.ods required manually editing
# of the included content.xml file
with pytest.raises(ValueError, match="Unrecognized type awesome_new_type"):
    pd.read_excel("invalid_value_type.ods")

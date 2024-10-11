# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string_arrow.py
msg = re.escape("Value must be one of python|pyarrow")
with pytest.raises(ValueError, match=msg):
    pd.options.mode.string_storage = "foo"

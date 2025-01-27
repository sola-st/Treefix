# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string_arrow.py
msg = re.escape("pyarrow>=6.0.0 is required for PyArrow backed")

with pytest.raises(ImportError, match=msg):
    StringDtype(storage="pyarrow")

with pytest.raises(ImportError, match=msg):
    ArrowStringArray([])

with pytest.raises(ImportError, match=msg):
    ArrowStringArray._from_sequence(["a", None, "b"])

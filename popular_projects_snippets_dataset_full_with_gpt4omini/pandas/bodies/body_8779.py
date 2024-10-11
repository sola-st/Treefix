# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string_arrow.py
with pd.option_context("string_storage", "python"):
    ArrowStringArray._from_sequence(["a", None, "c"], dtype="string")

with pd.option_context("string_storage", "pyarrow"):
    ArrowStringArray._from_sequence(["a", None, "c"], dtype="string")

with pytest.raises(AssertionError, match=None):
    ArrowStringArray._from_sequence(["a", None, "c"], dtype="string[python]")

ArrowStringArray._from_sequence(["a", None, "c"], dtype="string[pyarrow]")

with pytest.raises(AssertionError, match=None):
    with pd.option_context("string_storage", "python"):
        ArrowStringArray._from_sequence(["a", None, "c"], dtype=StringDtype())

with pd.option_context("string_storage", "pyarrow"):
    ArrowStringArray._from_sequence(["a", None, "c"], dtype=StringDtype())

with pytest.raises(AssertionError, match=None):
    ArrowStringArray._from_sequence(["a", None, "c"], dtype=StringDtype("python"))

ArrowStringArray._from_sequence(["a", None, "c"], dtype=StringDtype("pyarrow"))

with pd.option_context("string_storage", "python"):
    StringArray._from_sequence(["a", None, "c"], dtype="string")

with pd.option_context("string_storage", "pyarrow"):
    StringArray._from_sequence(["a", None, "c"], dtype="string")

StringArray._from_sequence(["a", None, "c"], dtype="string[python]")

with pytest.raises(AssertionError, match=None):
    StringArray._from_sequence(["a", None, "c"], dtype="string[pyarrow]")

with pd.option_context("string_storage", "python"):
    StringArray._from_sequence(["a", None, "c"], dtype=StringDtype())

with pytest.raises(AssertionError, match=None):
    with pd.option_context("string_storage", "pyarrow"):
        StringArray._from_sequence(["a", None, "c"], dtype=StringDtype())

StringArray._from_sequence(["a", None, "c"], dtype=StringDtype("python"))

with pytest.raises(AssertionError, match=None):
    StringArray._from_sequence(["a", None, "c"], dtype=StringDtype("pyarrow"))

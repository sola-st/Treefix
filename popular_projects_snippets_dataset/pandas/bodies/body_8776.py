# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string_arrow.py
with pd.option_context("string_storage", string_storage):
    assert StringDtype().storage == string_storage
    result = pd.array(["a", "b"])
    assert result.dtype.storage == string_storage

expected = (
    StringDtype(string_storage).construct_array_type()._from_sequence(["a", "b"])
)
tm.assert_equal(result, expected)

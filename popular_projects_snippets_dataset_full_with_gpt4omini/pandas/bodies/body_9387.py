# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
result = IntegerArray._from_sequence(["1", "2", None])
expected = pd.array([1, 2, np.nan], dtype="Int64")
tm.assert_extension_array_equal(result, expected)

with pytest.raises(
    ValueError, match=r"invalid literal for int\(\) with base 10: .*"
):
    IntegerArray._from_sequence(["1", "2", ""])

with pytest.raises(
    ValueError, match=r"invalid literal for int\(\) with base 10: .*"
):
    IntegerArray._from_sequence(["1.5", "2.0"])

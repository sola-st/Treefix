# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(
    ["ABC", "ＡＢＣ", "１２３", np.nan, "ｱｲｴ"],
    index=["a", "b", "c", "d", "e"],
    dtype=any_string_dtype,
)
with pytest.raises(ValueError, match="invalid normalization form"):
    ser.str.normalize("xxx")

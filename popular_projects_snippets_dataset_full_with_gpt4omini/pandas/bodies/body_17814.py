# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_inclusive.py
with pytest.raises(
    ValueError,
    match="Inclusive has to be either 'both', 'neither', 'left' or 'right'",
):
    validate_inclusive(invalid_inclusive)

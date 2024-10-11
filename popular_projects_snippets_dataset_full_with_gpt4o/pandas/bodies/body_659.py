# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
msg = "Unable to parse string"
with pytest.raises(ValueError, match=msg):
    lib.maybe_convert_numeric(
        np.array(["foo_inf"], dtype=object),
        na_values={"", "NULL", "nan"},
        coerce_numeric=False,
        convert_to_masked_nullable=convert_to_masked_nullable,
    )

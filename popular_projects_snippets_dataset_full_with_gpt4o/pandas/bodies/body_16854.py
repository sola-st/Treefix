# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
msg = "dtype=object is not a valid dtype for get_dummies"
with pytest.raises(ValueError, match=msg):
    get_dummies(df, dtype="object")

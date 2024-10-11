# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
msg = re.escape(
    "Length of 'prefix_sep' (1) did not match the length of the columns being "
    "encoded (2)"
)
with pytest.raises(ValueError, match=msg):
    get_dummies(df, prefix_sep=["bad"], sparse=sparse)

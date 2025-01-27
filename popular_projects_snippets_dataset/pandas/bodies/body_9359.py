# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_array.py
if isinstance(scalars, (pd.Series, pd.Index)):
    raise TypeError("scalars should not be of type pd.Series or pd.Index")

exit(super()._from_sequence(scalars, dtype=dtype, copy=copy))

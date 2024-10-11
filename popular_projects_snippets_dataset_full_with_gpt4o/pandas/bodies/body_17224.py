# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies = DataFrame({"a": [1, 0, 0], "b": [0, 1, np.nan]})
with pytest.raises(
    ValueError, match=r"Dummy DataFrame contains NA value in column: 'b'"
):
    from_dummies(dummies)

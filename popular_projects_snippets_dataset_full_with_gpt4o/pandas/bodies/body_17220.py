# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies = [0, 1, 0]
with pytest.raises(
    TypeError,
    match=r"Expected 'data' to be a 'DataFrame'; Received 'data' of type: list",
):
    from_dummies(dummies)

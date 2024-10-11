# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies = DataFrame({"a": [1, 0, 1], "b": [0, 1, 1]})
with pytest.raises(
    TypeError,
    match=(
        r"Expected 'default_category' to be of type 'None', 'Hashable', or 'dict'; "
        r"Received 'default_category' of type: list"
    ),
):
    from_dummies(dummies, default_category=["c", "d"])

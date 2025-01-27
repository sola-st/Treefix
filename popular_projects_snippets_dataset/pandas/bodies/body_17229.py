# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
with pytest.raises(
    TypeError,
    match=(
        r"Expected 'default_category' to be of type 'None', 'Hashable', or 'dict'; "
        r"Received 'default_category' of type: list"
    ),
):
    from_dummies(dummies_with_unassigned, sep="_", default_category=["x", "y"])

# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py

with pytest.raises(
    TypeError,
    match=(
        r"Expected 'sep' to be of type 'str' or 'None'; "
        r"Received 'sep' of type: list"
    ),
):
    from_dummies(dummies_basic, sep=["_"])

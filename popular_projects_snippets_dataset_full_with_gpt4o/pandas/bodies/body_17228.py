# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
with pytest.raises(
    ValueError,
    match=(
        r"Dummy DataFrame contains unassigned value\(s\); "
        r"First instance in row: 2"
    ),
):
    from_dummies(dummies_with_unassigned, sep="_")

# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies = DataFrame(
    {
        "col1_a": [1, 0, 1],
        "col1_b": [1, 1, 0],
        "col2_a": [0, 1, 0],
        "col2_b": [1, 0, 0],
        "col2_c": [0, 0, 1],
    },
)
with pytest.raises(
    ValueError,
    match=(
        r"Dummy DataFrame contains multi-assignment\(s\); "
        r"First instance in row: 0"
    ),
):
    from_dummies(dummies, sep="_")

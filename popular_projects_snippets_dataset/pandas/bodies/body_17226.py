# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies = DataFrame(
    {
        "col1_a": [1, 0, 1],
        "col1_b": [0, 1, 0],
        "col2-a": [0, 1, 0],
        "col2-b": [1, 0, 1],
    },
)
with pytest.raises(
    ValueError,
    match=(r"Separator not specified for column: col2-a"),
):
    from_dummies(dummies, sep="_")

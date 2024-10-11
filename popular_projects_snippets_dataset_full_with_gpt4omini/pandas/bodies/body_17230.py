# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
with pytest.raises(
    ValueError,
    match=(
        r"Length of 'default_category' \(1\) did not match "
        r"the length of the columns being encoded \(2\)"
    ),
):
    from_dummies(dummies_with_unassigned, sep="_", default_category={"col1": "x"})

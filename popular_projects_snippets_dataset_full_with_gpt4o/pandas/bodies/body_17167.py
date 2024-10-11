# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# see gh-3335
msg = (
    f'Conflicting name "{margin_name}" in margins|'
    "margins_name argument must be a string"
)
with pytest.raises(ValueError, match=msg):
    # multi-index index
    pivot_table(
        data,
        values="D",
        index=["A", "B"],
        columns=["C"],
        margins=True,
        margins_name=margin_name,
    )
with pytest.raises(ValueError, match=msg):
    # multi-index column
    pivot_table(
        data,
        values="D",
        index=["C"],
        columns=["A", "B"],
        margins=True,
        margins_name=margin_name,
    )
with pytest.raises(ValueError, match=msg):
    # non-multi-index index/column
    pivot_table(
        data,
        values="D",
        index=["A"],
        columns=["B"],
        margins=True,
        margins_name=margin_name,
    )

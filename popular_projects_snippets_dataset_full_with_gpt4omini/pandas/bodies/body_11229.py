# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# per GH 23566 enforced deprecation raises a ValueError
with pytest.raises(ValueError, match="Cannot subset columns with a tuple"):
    df.groupby("A")["C", "D"].mean()

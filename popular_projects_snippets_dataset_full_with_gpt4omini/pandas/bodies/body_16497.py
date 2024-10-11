# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
df = DataFrame(
    {
        "A2010": [1.0, 2.0],
        "A2011": [3.0, 4.0],
        "B2010": [5.0, 6.0],
        "A": ["X1", "X2"],
    }
)
msg = "stubname can't be identical to a column name"
with pytest.raises(ValueError, match=msg):
    wide_to_long(df, ["A", "B"], i="A", j="colname")

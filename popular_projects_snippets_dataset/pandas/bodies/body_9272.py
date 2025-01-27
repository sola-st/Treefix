# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py

# Cannot have NaN in categories
msg = "Categorical categories cannot be null"
with pytest.raises(ValueError, match=msg):
    Categorical([np.nan, "a", "b", "c"], categories=[np.nan, "a", "b", "c"])

with pytest.raises(ValueError, match=msg):
    Categorical([None, "a", "b", "c"], categories=[None, "a", "b", "c"])

with pytest.raises(ValueError, match=msg):
    Categorical(
        DatetimeIndex(["nat", "20160101"]),
        categories=[NaT, Timestamp("20160101")],
    )

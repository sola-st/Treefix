# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_subclass.py
# GH28330 -- preserve subclass through groupby.resample()

df = obj(
    {
        "Buyer": "Carl Carl Carl Carl Joe Carl".split(),
        "Quantity": [18, 3, 5, 1, 9, 3],
        "Date": [
            datetime(2013, 9, 1, 13, 0),
            datetime(2013, 9, 1, 13, 5),
            datetime(2013, 10, 1, 20, 0),
            datetime(2013, 10, 3, 10, 0),
            datetime(2013, 12, 2, 12, 0),
            datetime(2013, 9, 2, 14, 0),
        ],
    }
)
df = df.set_index("Date")

# Confirm groupby.resample() preserves dataframe type
result = df.groupby("Buyer").resample("5D").sum()
assert isinstance(result, obj)

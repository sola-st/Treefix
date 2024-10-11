# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH 3881
# make sure API of timegrouper conforms

df = DataFrame(
    {
        "Branch": "A A A A A B".split(),
        "Buyer": "Carl Mark Carl Joe Joe Carl".split(),
        "Quantity": [1, 3, 5, 8, 9, 3],
        "Date": [
            datetime(2013, 1, 1, 13, 0),
            datetime(2013, 1, 1, 13, 5),
            datetime(2013, 10, 1, 20, 0),
            datetime(2013, 10, 2, 10, 0),
            datetime(2013, 12, 2, 12, 0),
            datetime(2013, 12, 2, 14, 0),
        ],
    }
)

if should_sort:
    df = df.sort_values(by="Quantity", ascending=False)

df = df.set_index("Date", drop=False)
g = df.groupby(Grouper(freq="6M"))
assert g.group_keys

assert isinstance(g.grouper, BinGrouper)
groups = g.groups
assert isinstance(groups, dict)
assert len(groups) == 3

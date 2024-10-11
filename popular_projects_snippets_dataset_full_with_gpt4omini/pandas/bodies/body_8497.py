# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
dti = date_range(start="1/1/2005", end="12/1/2005", freq="M")
dti2 = dti[[1, 3, 5]]

v1 = dti2[0]
v2 = dti2[1]
v3 = dti2[2]

assert v1 == Timestamp("2/28/2005")
assert v2 == Timestamp("4/30/2005")
assert v3 == Timestamp("6/30/2005")

# getitem with non-slice drops freq
assert dti2.freq is None

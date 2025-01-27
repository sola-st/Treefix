# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_astype.py
# astype to categorical and back should preserve date objects
v = date.today()

obj = Index([v, v])
assert obj.dtype == object

cat = obj.astype("category")

rtrip = cat.astype(object)
assert rtrip.dtype == object
assert type(rtrip[0]) is date

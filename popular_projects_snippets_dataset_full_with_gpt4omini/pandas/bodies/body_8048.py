# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
casted = index.astype("i8")

# it works!
casted.get_loc(5)

# pass on name
index.name = "foobar"
casted = index.astype("i8")
assert casted.name == "foobar"

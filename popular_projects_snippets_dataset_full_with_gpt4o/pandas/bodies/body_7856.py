# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_to_timestamp.py
index = period_range(freq="A", start="1/1/2001", end="12/1/2009", name="foo")
assert index.name == "foo"

conv = index.to_timestamp("D")
assert conv.name == "foo"

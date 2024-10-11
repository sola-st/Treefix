# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
create_index = lambda: period_range(freq="A", start="1/1/2001", end="12/1/2009")
index = create_index()
assert index.is_(index)
assert not index.is_(create_index())
assert index.is_(index.view())
assert index.is_(index.view().view().view().view().view())
assert index.view().is_(index)
ind2 = index.view()
index.name = "Apple"
assert ind2.is_(index)
assert not index.is_(index[:])
assert not index.is_(index.asfreq("M"))
assert not index.is_(index.asfreq("A"))

assert not index.is_(index - 2)
assert not index.is_(index - 0)

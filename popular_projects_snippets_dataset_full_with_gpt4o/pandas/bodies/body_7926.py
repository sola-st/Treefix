# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
idx = period_range("2000-1-1", freq="A", periods=10)
bad_period = Period("2012", "A")
with pytest.raises(KeyError, match=r"^Period\('2012', 'A-DEC'\)$"):
    idx.get_loc(bad_period)

try:
    idx.get_loc(bad_period)
except KeyError as inst:
    assert inst.args[0] == bad_period

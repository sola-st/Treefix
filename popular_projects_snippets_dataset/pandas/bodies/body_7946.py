# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# GH 17717
p0 = Period("2017-09-01")
p1 = Period("2017-09-02")
p2 = Period("2017-09-03")
p3 = Period("2017-09-04")

ps0 = [p0, p1, p2]
idx0 = PeriodIndex(ps0)

for p in ps0:
    assert p in idx0
    assert str(p) in idx0

# GH#31172
# Higher-resolution period-like are _not_ considered as contained
key = "2017-09-01 00:00:01"
assert key not in idx0
with pytest.raises(KeyError, match=key):
    idx0.get_loc(key)

assert "2017-09" in idx0

assert p3 not in idx0

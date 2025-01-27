# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_tools.py
index = period_range(freq="A", start="1/1/2001", end="12/1/2009")
rs = index.tolist()
for x in rs:
    assert isinstance(x, Period)

recon = PeriodIndex(rs)
tm.assert_index_equal(index, recon)

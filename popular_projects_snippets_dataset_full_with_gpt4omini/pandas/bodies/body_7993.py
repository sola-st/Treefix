# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_join.py
index = period_range("1/1/2000", "1/20/2000", freq="D")
index3 = period_range("1/1/2000", "1/20/2000", freq="2D")
msg = r".*Input has different freq=2D from Period\(freq=D\)"
with pytest.raises(IncompatibleFrequency, match=msg):
    index.join(index3)

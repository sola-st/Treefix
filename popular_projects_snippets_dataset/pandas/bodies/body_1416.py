# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH 14424

df = DataFrame()
assert not df.index._is_all_dates
with pytest.raises(KeyError, match="'2011'"):
    df["2011"]

with pytest.raises(KeyError, match="^0$"):
    df.loc["2011", 0]

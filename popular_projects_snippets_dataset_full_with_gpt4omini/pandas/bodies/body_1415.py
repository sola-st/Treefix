# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH 14424
# string indexing against datetimelike with object
# dtype should properly raises KeyError
df = DataFrame([1], Index([pd.Timestamp("2011-01-01")], dtype=object))
assert df.index._is_all_dates
with pytest.raises(KeyError, match="'2011'"):
    df["2011"]

with pytest.raises(KeyError, match="'2011'"):
    df.loc["2011", 0]

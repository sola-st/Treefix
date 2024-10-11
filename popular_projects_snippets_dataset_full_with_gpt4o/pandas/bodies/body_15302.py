# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_datetime.py
idx = date_range("2001-1-1", periods=20, freq="M")
ts = Series(np.random.rand(len(idx)), index=idx)

# getting

# GH 3070, make sure semantics work on Series/Frame
expected = ts["2001"]
expected.name = "A"

df = DataFrame({"A": ts})

# GH#36179 pre-2.0 df["2001"] operated as slicing on rows. in 2.0 it behaves
#  like any other key, so raises
with pytest.raises(KeyError, match="2001"):
    df["2001"]

# setting
ts["2001"] = 1
expected = ts["2001"]
expected.name = "A"

df.loc["2001", "A"] = 1

with pytest.raises(KeyError, match="2001"):
    df["2001"]

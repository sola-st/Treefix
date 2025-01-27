# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
# GH#46904
np.random.seed(1234)
index = date_range(datetime(2005, 1, 1), datetime(2005, 1, 10), freq="D")
index.name = "date"
df = DataFrame(np.random.rand(10, 2), columns=list("AB"), index=index).T
res = df.resample("M", axis=1)
with pytest.raises(NotImplementedError, match="axis other than 0 is not supported"):
    res.agg(func)

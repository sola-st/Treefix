# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py

# make sure that we are consistent across
# similar aggregations with and w/o selection list
df = DataFrame(
    np.random.randn(1000, 3),
    index=date_range("1/1/2012", freq="S", periods=1000),
    columns=["A", "B", "C"],
)

r = df.resample("3T")

msg = r"Column\(s\) \['r1', 'r2'\] do not exist"
with pytest.raises(KeyError, match=msg):
    r.agg({"r1": "mean", "r2": "sum"})

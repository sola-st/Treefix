# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
# GH#39025
df = DataFrame(
    np.random.randn(1000, 2),
    index=date_range("1/1/2012", freq="S", periods=1000),
    columns=[1, "a"],
)

r = df.resample("3T")

msg = r"Column\(s\) \[2, 'b'\] do not exist"
with pytest.raises(KeyError, match=msg):
    r.agg({2: "mean", "b": "sum"})

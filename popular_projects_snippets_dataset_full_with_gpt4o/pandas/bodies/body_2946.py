# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
df = DataFrame({"A": [1, 2, np.nan, 4], "B": [np.nan, 2, 3, 4]})
df = df.set_index("A")
msg = (
    "Interpolation with NaNs in the index has not been implemented. "
    "Try filling those NaNs before interpolating."
)
with pytest.raises(NotImplementedError, match=msg):
    df.interpolate(method="values")

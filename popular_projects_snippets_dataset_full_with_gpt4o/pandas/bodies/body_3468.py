# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
interpolation, method = interp_method
q = DataFrame({"x": [], "y": []}).quantile(
    0.1, axis=0, numeric_only=True, interpolation=interpolation, method=method
)
assert np.isnan(q["x"]) and np.isnan(q["y"])

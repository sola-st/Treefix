# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
cat = Categorical(["a", "b", "c", "b"], ordered=True)
msg = (
    f"the '{kwarg}' parameter is not supported in the pandas implementation "
    f"of {method}"
)
if kwarg == "axis":
    msg = r"`axis` must be fewer than the number of dimensions \(1\)"
kwargs = {kwarg: 42}
method = getattr(np, method)
with pytest.raises(ValueError, match=msg):
    method(cat, **kwargs)

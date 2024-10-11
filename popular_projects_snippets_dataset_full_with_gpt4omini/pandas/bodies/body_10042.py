# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
df = DataFrame({"A": ["a", "b", "a", "b"], "B": range(4)})
with pytest.raises(ValueError, match="engine must be either"):
    getattr(grouper(df).ewm(com=1.0), method)(engine="foo")

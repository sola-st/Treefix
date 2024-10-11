# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
with pytest.raises(ValueError, match="Invalid method: foo"):
    DataFrame(range(1)).quantile(0.5, method="foo")

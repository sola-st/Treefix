# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
with pytest.raises(ValueError, match="method must be 'table' or 'single"):
    Series(range(1)).rolling(1, method="foo")

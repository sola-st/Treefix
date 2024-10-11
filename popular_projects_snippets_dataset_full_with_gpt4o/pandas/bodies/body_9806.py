# Extracted from ./data/repos/pandas/pandas/tests/window/conftest.py
"""Make mocked frame as fixture."""
exit(DataFrame(
    np.random.randn(100, 10),
    index=bdate_range(datetime(2009, 1, 1), periods=100),
))

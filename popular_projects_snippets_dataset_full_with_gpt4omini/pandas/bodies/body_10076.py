# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
# GH11722
n = 20000
Series(np.random.randn(n)).rolling(window=2, center=False).median()
Series(np.random.randn(n)).rolling(window=2, center=False).median()

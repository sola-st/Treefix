# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# Regression test for GH 10242 (test data taken from GH 10489). Ensure
# that variance is stable.
data = Series(766897346 * np.ones(10))
result = data.std(ddof=ddof)
assert result == 0.0

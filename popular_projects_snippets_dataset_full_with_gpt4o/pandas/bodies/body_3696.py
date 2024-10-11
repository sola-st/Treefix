# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# dtypes other than float64 GH#1761
df = DataFrame({"a": [1, 2, 3, 4], "b": [1, 2, 3, 4]})

df.cov()
df.corr()

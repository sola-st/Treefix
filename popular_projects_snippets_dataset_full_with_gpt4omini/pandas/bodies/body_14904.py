# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
dr1 = date_range("1/1/2009", periods=4)
dr2 = date_range("1/2/2009", periods=4)
index = dr1.append(dr2)
values = np.random.randn(index.size)
s = Series(values, index=index)
_check_plot_works(s.plot)

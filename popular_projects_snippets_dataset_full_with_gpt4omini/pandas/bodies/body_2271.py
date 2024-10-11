# Extracted from ./data/repos/pandas/pandas/tests/frame/test_cumulative.py
# it works
df = DataFrame({"A": np.arange(20)}, index=np.arange(20))
df.cummax()
df.cummin()
df.cumsum()

dm = DataFrame(np.arange(20).reshape(4, 5), index=range(4), columns=range(5))
# TODO(wesm): do something with this?
dm.cumsum()

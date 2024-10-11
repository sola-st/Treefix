# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
from matplotlib.pyplot import (
    gcf,
    subplot,
)

x = Series(np.random.randn(2))
y = Series(np.random.randn(2))
subplot(121)
x.hist()
subplot(122)
y.hist()
fig = gcf()
axes = fig.axes
assert len(axes) == 2

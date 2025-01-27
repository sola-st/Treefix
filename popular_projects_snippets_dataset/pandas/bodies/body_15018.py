# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
from pylab import figure

fig1 = figure()
fig2 = figure()
ax1 = fig1.add_subplot(111)
msg = "passed axis not bound to passed figure"
with pytest.raises(AssertionError, match=msg):
    ts.hist(ax=ax1, figure=fig2)

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
from l3.Runtime import _l_
x = date_range(start="2012-01-02", periods=10, freq="D")
_l_(20602)
y = list(range(len(x)))
_l_(20603)
_, ax = self.plt.subplots()
_l_(20604)
lines = ax.plot(x, y, label="Y")
_l_(20605)
tm.assert_index_equal(DatetimeIndex(lines[0].get_xdata()), x)
_l_(20606)

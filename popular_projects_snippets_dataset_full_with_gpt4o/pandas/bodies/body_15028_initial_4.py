import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import DataFrame, to_datetime # pragma: no cover
import matplotlib.pyplot as plt # pragma: no cover
import matplotlib.ticker as ticker # pragma: no cover

def _check_plot_works(func, *args, **kwargs):# pragma: no cover
    if "default_axes" in kwargs and kwargs["default_axes"] == True:# pragma: no cover
        fig, axes = plt.subplots()# pragma: no cover
        kwargs["ax"] = axes# pragma: no cover
        func(*args, **kwargs)# pragma: no cover
    else:# pragma: no cover
        func(*args, **kwargs) # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.plt = plt# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover
matplotlib.use('Agg') # pragma: no cover
matplotlib.use('Agg')# pragma: no cover
tm = type('Mock', (object,), {'close': plt.close}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
from l3.Runtime import _l_
df = DataFrame(np.random.randn(100, 2))
_l_(22167)
df[2] = to_datetime(
    np.random.randint(
        812419200000000000,
        819331200000000000,
        size=100,
        dtype=np.int64,
    )
)
_l_(22168)
# Use default_axes=True when plotting method generate subplots itself
_check_plot_works(df.hist, default_axes=True)
_l_(22169)
self.plt.tight_layout()
_l_(22170)

tm.close()
_l_(22171)
